from app.models.subject import Subject
from app.models.exam_paper import ExamPaper

def test_new_exam_paper(session):
    """
    GIVEN un modèle ExamPaper
    WHEN on crée une nouvelle annale
    THEN vérifier que les champs sont correctement définis
    """
    subject = Subject(name='Mathématiques Test 1')
    session.add(subject)
    session.commit()

    exam_paper = ExamPaper(
        title='Bac 2024',
        year=2024,
        pdf_url='https://example.com/bac2024.pdf',
        subject=subject
    )
    session.add(exam_paper)
    session.commit()

    assert exam_paper.title == 'Bac 2024'
    assert exam_paper.year == 2024
    assert exam_paper.pdf_url == 'https://example.com/bac2024.pdf'
    assert exam_paper.subject == subject
    assert exam_paper.created_at is not None
    assert exam_paper.updated_at is not None

def test_exam_paper_representation(session):
    """
    GIVEN un modèle ExamPaper
    WHEN on affiche l'annale
    THEN vérifier que la représentation est correcte
    """
    subject = Subject(name='Mathématiques Test 2')
    session.add(subject)
    session.commit()

    exam_paper = ExamPaper(
        title='Bac 2023',
        year=2023,
        pdf_url='https://example.com/bac2023.pdf',
        subject=subject
    )
    session.add(exam_paper)
    session.commit()

    assert str(exam_paper) == '<ExamPaper Bac 2023>'

def test_exam_paper_subject_relationship(session):
    """
    GIVEN un modèle ExamPaper
    WHEN on crée une annale liée à une matière
    THEN vérifier que la relation bidirectionnelle fonctionne
    """
    subject = Subject(name='Mathématiques Test 3')
    session.add(subject)
    session.commit()

    exam_paper = ExamPaper(
        title='Bac 2022',
        year=2022,
        pdf_url='https://example.com/bac2022.pdf',
        subject=subject
    )
    session.add(exam_paper)
    session.commit()

    assert exam_paper in subject.exam_papers
    assert exam_paper.subject == subject 