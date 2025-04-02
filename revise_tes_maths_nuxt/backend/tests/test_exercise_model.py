import pytest
from app import db
from app.models.exercise import Exercise
from app.models.exam_paper import ExamPaper

def test_new_exercise(session):
    """
    GIVEN un modèle Exercise
    WHEN un nouvel exercice est créé
    THEN vérifier que les champs sont correctement définis
    """
    # Création des données nécessaires
    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf'
    )
    session.add(exam_paper)
    session.commit()

    exercise = Exercise(
        number=1,
        description='Calculer la probabilité...',
        themes=['Probabilités et Statistiques'],
        exam_paper=exam_paper
    )
    session.add(exercise)
    session.commit()

    assert exercise.number == 1
    assert exercise.description == 'Calculer la probabilité...'
    assert exercise.themes == ['Probabilités et Statistiques']
    assert exercise.exam_paper == exam_paper
    assert exercise.created_at is not None
    assert exercise.updated_at is not None

def test_exercise_representation(session):
    """
    GIVEN un modèle Exercise
    WHEN on affiche l'exercice
    THEN vérifier que la représentation est correcte
    """
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

    assert str(exercise) == '<Exercise 2>'

def test_exercise_exam_paper_relationship(session):
    """
    GIVEN un modèle Exercise
    WHEN on crée un exercice lié à une annale
    THEN vérifier que la relation bidirectionnelle fonctionne
    """
    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf'
    )
    session.add(exam_paper)
    session.commit()

    exercise = Exercise(
        number=3,
        description='Étudier la fonction...',
        themes=['Analyse'],
        exam_paper=exam_paper
    )
    session.add(exercise)
    session.commit()

    assert exercise in exam_paper.exercises
    assert exercise.exam_paper == exam_paper 