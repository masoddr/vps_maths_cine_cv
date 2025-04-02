import pytest
from datetime import datetime
from app import db
from app.models.progress import Progress
from app.models.user import User
from app.models.exercise import Exercise
from app.models.exam_paper import ExamPaper

def test_new_progress(session):
    """
    GIVEN un modèle Progress
    WHEN une nouvelle progression est créée
    THEN vérifier que les champs sont correctement définis
    """
    # Création des données nécessaires
    user = User(
        email='test@example.com',
        first_name='Test',
        last_name='User'
    )
    user.set_password('password123')
    session.add(user)
    
    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf'
    )
    session.add(exam_paper)
    
    exercise = Exercise(
        number=1,
        description='Calculer la probabilité...',
        themes=['Probabilités et Statistiques'],
        exam_paper=exam_paper
    )
    session.add(exercise)
    session.commit()

    progress = Progress(
        user=user,
        exercise=exercise,
        status='completed',
        time_spent=30,  # minutes
        notes='Exercice bien compris'
    )
    session.add(progress)
    session.commit()

    assert progress.user == user
    assert progress.exercise == exercise
    assert progress.status == 'completed'
    assert progress.time_spent == 30
    assert progress.notes == 'Exercice bien compris'
    assert progress.created_at is not None
    assert progress.updated_at is not None

def test_progress_representation(session):
    """
    GIVEN un modèle Progress
    WHEN on affiche la progression
    THEN vérifier que la représentation est correcte
    """
    user = User(
        email='test2@example.com',
        first_name='Test',
        last_name='User'
    )
    user.set_password('password123')
    session.add(user)
    
    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf'
    )
    session.add(exam_paper)
    
    exercise = Exercise(
        number=2,
        description='Démontrer que...',
        themes=['Géométrie'],
        exam_paper=exam_paper
    )
    session.add(exercise)
    session.commit()

    progress = Progress(
        user=user,
        exercise=exercise,
        status='in_progress'
    )
    session.add(progress)
    session.commit()

    assert str(progress) == f'<Progress User: {user.email}, Exercise: {exercise.number}, Status: in_progress>'

def test_progress_relationships(session):
    """
    GIVEN un modèle Progress
    WHEN on crée une progression liée à un utilisateur et un exercice
    THEN vérifier que les relations bidirectionnelles fonctionnent
    """
    user = User(
        email='test3@example.com',
        first_name='Test',
        last_name='User'
    )
    user.set_password('password123')
    session.add(user)
    
    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf'
    )
    session.add(exam_paper)
    
    exercise = Exercise(
        number=3,
        description='Étudier la fonction...',
        themes=['Analyse'],
        exam_paper=exam_paper
    )
    session.add(exercise)
    session.commit()

    progress = Progress(
        user=user,
        exercise=exercise,
        status='not_started'
    )
    session.add(progress)
    session.commit()

    assert progress in user.progress
    assert progress in exercise.progress
    assert progress.user == user
    assert progress.exercise == exercise

def test_progress_status_validation(session):
    """
    GIVEN un modèle Progress
    WHEN on essaie de définir un statut invalide
    THEN vérifier que cela lève une ValueError
    """
    user = User(
        email='test4@example.com',
        first_name='Test',
        last_name='User'
    )
    user.set_password('password123')
    session.add(user)
    
    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf'
    )
    session.add(exam_paper)
    
    exercise = Exercise(
        number=4,
        description='Étudier la fonction...',
        themes=['Analyse'],
        exam_paper=exam_paper
    )
    session.add(exercise)
    session.commit()

    with pytest.raises(ValueError) as excinfo:
        progress = Progress(
            user=user,
            exercise=exercise,
            status='invalid_status'
        )
        session.add(progress)
        session.commit()

    assert "Invalid status" in str(excinfo.value) 