import json
import pytest
from app.models.exam_paper import ExamPaper
from app.models.exercise import Exercise
from app.models.progress import Progress

def test_get_progress_unauthorized(client):
    """
    GIVEN l'application Flask configurée pour les tests
    WHEN la route '/api/progress' est appelée sans authentification (GET)
    THEN vérifier que l'accès est refusé
    """
    response = client.get('/api/progress')
    assert response.status_code == 401  # Non autorisé

def test_get_progress_list(client, test_user, session):
    """
    GIVEN un utilisateur connecté avec des exercices en cours
    WHEN la route '/api/progress' est appelée (GET)
    THEN vérifier que la liste des progressions est retournée
    """
    # Créer les données nécessaires
    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf'
    )
    session.add(exam_paper)
    session.commit()
    
    exercise = Exercise(
        number=1,
        description='Démontrer que...',
        themes=['Géométrie'],
        exam_paper=exam_paper
    )
    session.add(exercise)
    session.commit()
    
    progress = Progress(
        user=test_user,
        exercise=exercise,
        status='in_progress',
        time_spent=15
    )
    session.add(progress)
    session.commit()
    
    # Connecter l'utilisateur
    client.post(
        '/api/login',
        data=json.dumps({
            'email': 'test@example.com',
            'password': 'password123'
        }),
        content_type='application/json'
    )
    
    response = client.get('/api/progress')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['status'] == 'in_progress'
    assert data[0]['time_spent'] == 15

def test_update_progress(client, test_user, session):
    """
    GIVEN un utilisateur connecté
    WHEN la route '/api/progress/<exercise_id>' est appelée (PUT)
    THEN vérifier que la progression est mise à jour
    """
    # Créer les données nécessaires
    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf'
    )
    session.add(exam_paper)
    session.commit()
    
    exercise = Exercise(
        number=2,
        description='Démontrer que...',
        themes=['Géométrie'],
        exam_paper=exam_paper
    )
    session.add(exercise)
    session.commit()
    
    # Connecter l'utilisateur
    client.post(
        '/api/login',
        data=json.dumps({
            'email': 'test@example.com',
            'password': 'password123'
        }),
        content_type='application/json'
    )
    
    # Mettre à jour la progression
    data = {
        'status': 'completed',
        'time_spent': 30
    }
    
    response = client.put(
        f'/api/progress/{exercise.id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result['status'] == 'completed'
    assert result['time_spent'] == 30

def test_invalid_status(client, test_user, session):
    """
    GIVEN un utilisateur connecté
    WHEN la route '/api/progress/<exercise_id>' est appelée avec un statut invalide
    THEN vérifier que l'erreur est gérée correctement
    """
    # Créer les données nécessaires
    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf'
    )
    session.add(exam_paper)
    session.commit()
    
    exercise = Exercise(
        number=3,
        description='Démontrer que...',
        themes=['Géométrie'],
        exam_paper=exam_paper
    )
    session.add(exercise)
    session.commit()
    
    # Connecter l'utilisateur
    client.post(
        '/api/login',
        data=json.dumps({
            'email': 'test@example.com',
            'password': 'password123'
        }),
        content_type='application/json'
    )
    
    # Tenter de créer une progression avec un statut invalide
    data = {
        'status': 'invalid_status',
        'time_spent': 5
    }
    
    response = client.post(
        f'/api/progress/{exercise.id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code == 400
    result = json.loads(response.data)
    assert 'error' in result
    assert 'Statut invalide' in result['error'] 