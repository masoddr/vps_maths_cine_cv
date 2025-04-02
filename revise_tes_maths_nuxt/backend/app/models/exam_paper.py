from datetime import datetime, UTC
from app import db

class ExamPaper(db.Model):
    """Modèle représentant une annale d'examen"""
    
    __tablename__ = 'exam_paper'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    session = db.Column(db.String(64), nullable=True)  # e.g., 'normale', 'rattrapage'
    level = db.Column(db.String(64), nullable=True)  # e.g., 'terminale', 'première'
    pdf_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    # Relation avec Exercise
    exercises = db.relationship('Exercise', back_populates='exam_paper', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<ExamPaper {self.title}>' 