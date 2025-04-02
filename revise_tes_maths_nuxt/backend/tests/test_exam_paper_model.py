import pytest
from app import db
from app.models.exam_paper import ExamPaper

def test_new_exam_paper(session):
    """
    GIVEN un modèle ExamPaper
    WHEN on crée une nouvelle annale
    THEN vérifier que les champs sont correctement définis
    """
    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf'
    )
    session.add(exam_paper)
    session.commit()

    assert exam_paper.title == 'Bac 2024'
    assert exam_paper.year == 2024
    assert exam_paper.pdf_url == 'https://example.com/bac2024.pdf'
    assert exam_paper.created_at is not None
    assert exam_paper.updated_at is not None

def test_exam_paper_representation(session):
    """
    GIVEN un modèle ExamPaper
    WHEN on affiche l'annale
    THEN vérifier que la représentation est correcte
    """
    exam_paper = ExamPaper(
        title='Bac 2023',
        year=2023,
        pdf_url='https://example.com/bac2023.pdf'
    )
    session.add(exam_paper)
    session.commit()

    assert str(exam_paper) == '<ExamPaper Bac 2023>' 