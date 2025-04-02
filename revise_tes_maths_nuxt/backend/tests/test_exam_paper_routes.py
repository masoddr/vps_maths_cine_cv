import json
import pytest
import os
from io import BytesIO
from app.models.exam_paper import ExamPaper
from app.models.user import User

def test_get_exam_papers_list(client, session):
    """
    GIVEN l'application Flask configurée pour les tests
    WHEN la route '/api/exampapers' est appelée (GET)
    THEN vérifier que la liste des annales est retournée
    """
    # Créer quelques annales
    exam_papers = [
        ExamPaper(
            title='Bac 2024 - Métropole',
            year=2024,
            pdf_url='/static/uploads/pdfs/test1.pdf'
        ),
        ExamPaper(
            title='Bac 2023 - Antilles',
            year=2023,
            pdf_url='/static/uploads/pdfs/test2.pdf'
        )
    ]
    for paper in exam_papers:
        session.add(paper)
    session.commit()

    response = client.get('/api/exampapers')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) == 2  # Vérifier que nous avons bien 2 annales

def test_get_exam_papers_with_filters(client, session):
    """
    GIVEN des annales dans la base de données
    WHEN la route '/api/exampapers' est appelée avec des filtres
    THEN vérifier que les annales filtrées sont retournées
    """
    # Créer quelques annales
    exam_papers = [
        ExamPaper(
            title='Bac 2024 - Métropole',
            year=2024,
            pdf_url='/static/uploads/pdfs/test1.pdf'
        ),
        ExamPaper(
            title='Bac 2023 - Antilles',
            year=2023,
            pdf_url='/static/uploads/pdfs/test2.pdf'
        )
    ]
    for paper in exam_papers:
        session.add(paper)
    session.commit()

    # Test filtre par année
    response = client.get('/api/exampapers?year=2024')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['year'] == 2024

def test_get_exam_paper_detail(client, session):
    """
    GIVEN une annale dans la base de données
    WHEN la route '/api/exampapers/{id}' est appelée (GET)
    THEN vérifier que les détails de l'annale sont retournés
    """
    exam_paper = ExamPaper(
        title='Bac 2024 - Métropole',
        year=2024,
        pdf_url='/static/uploads/pdfs/test3.pdf'
    )
    session.add(exam_paper)
    session.commit()

    response = client.get(f'/api/exampapers/{exam_paper.id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == 'Bac 2024 - Métropole'
    assert data['year'] == 2024

def test_create_exam_paper_admin(client, session, tmp_path):
    """
    GIVEN un administrateur authentifié
    WHEN la route '/api/exampapers' est appelée (POST)
    THEN vérifier que l'annale est créée
    """
    # Créer un admin
    admin = User(
        email='admin@example.com',
        first_name='Admin',
        last_name='User',
        is_admin=True
    )
    admin.set_password('admin123')
    session.add(admin)
    session.commit()

    # Connecter l'admin
    client.post(
        '/api/login',
        data=json.dumps({
            'email': 'admin@example.com',
            'password': 'admin123'
        }),
        content_type='application/json'
    )

    # Créer une nouvelle annale avec un PDF
    data = {
        'title': 'Bac 2024 - Nouvelle Calédonie',
        'year': '2024',
        'exercises': json.dumps([{
            'number': 1,
            'themes': ['Analyse']
        }])
    }
    pdf = (BytesIO(b"test pdf content"), 'test.pdf')
    
    response = client.post(
        '/api/exampapers',
        data={**data, 'pdf': pdf},
        content_type='multipart/form-data'
    )
    
    assert response.status_code == 201
    result = json.loads(response.data)
    assert result['title'] == data['title']
    assert result['year'] == int(data['year'])
    assert result['pdf_url'].startswith('/static/uploads/pdfs/')
    assert result['pdf_url'].endswith('.pdf')

def test_update_exam_paper(client, session, tmp_path):
    """
    GIVEN un administrateur authentifié et une annale existante
    WHEN la route '/api/exampapers/{id}' est appelée (PUT)
    THEN vérifier que l'annale est mise à jour
    """
    # Créer un admin et le connecter
    admin = User(
        email='admin2@example.com',
        first_name='Admin',
        last_name='User',
        is_admin=True
    )
    admin.set_password('admin123')
    session.add(admin)
    session.commit()

    # Créer un fichier PDF temporaire pour le test
    pdf_path = os.path.join(tmp_path, 'test4.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(b"test pdf content")

    exam_paper = ExamPaper(
        title='Bac 2024 - Métropole',
        year=2024,
        pdf_url='/static/uploads/pdfs/test4.pdf'
    )
    session.add(exam_paper)
    session.commit()

    # Connecter l'admin
    client.post(
        '/api/login',
        data=json.dumps({
            'email': 'admin2@example.com',
            'password': 'admin123'
        }),
        content_type='application/json'
    )

    # Mettre à jour l'annale avec un nouveau PDF
    data = {
        'title': 'Bac 2024 - Métropole (Mise à jour)',
        'year': '2024'
    }
    pdf = (BytesIO(b"updated pdf content"), 'updated.pdf')
    
    response = client.put(
        f'/api/exampapers/{exam_paper.id}',
        data={**data, 'pdf': pdf},
        content_type='multipart/form-data'
    )
    
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result['title'] == data['title']
    
    # Vérifier que le contenu du PDF a été mis à jour
    pdf_response = client.get(f'/api/exampapers/{exam_paper.id}/pdf')
    assert pdf_response.status_code == 200
    assert pdf_response.data == b"updated pdf content"

def test_delete_exam_paper(client, session, tmp_path):
    """
    GIVEN un administrateur authentifié et une annale existante
    WHEN la route '/api/exampapers/{id}' est appelée (DELETE)
    THEN vérifier que l'annale est supprimée
    """
    # Créer un admin et le connecter
    admin = User(
        email='admin3@example.com',
        first_name='Admin',
        last_name='User',
        is_admin=True
    )
    admin.set_password('admin123')
    session.add(admin)
    session.commit()

    # Créer un fichier PDF temporaire pour le test
    pdf_path = os.path.join(tmp_path, 'test5.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(b"test pdf content")

    exam_paper = ExamPaper(
        title='Bac 2024 - À supprimer',
        year=2024,
        pdf_url='/static/uploads/pdfs/test5.pdf'
    )
    session.add(exam_paper)
    session.commit()

    # Connecter l'admin
    client.post(
        '/api/login',
        data=json.dumps({
            'email': 'admin3@example.com',
            'password': 'admin123'
        }),
        content_type='application/json'
    )

    # Supprimer l'annale
    response = client.delete(f'/api/exampapers/{exam_paper.id}')
    assert response.status_code == 200

    # Vérifier que l'annale a été supprimée
    check_response = client.get(f'/api/exampapers/{exam_paper.id}')
    assert check_response.status_code == 404 