from datetime import datetime, UTC
from app import db

class Exercise(db.Model):
    """Modèle représentant un exercice d'une annale"""
    
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    themes = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    # Clé étrangère vers ExamPaper
    exam_paper_id = db.Column(db.Integer, db.ForeignKey('exam_paper.id'), nullable=False)
    exam_paper = db.relationship('ExamPaper', back_populates='exercises')

    # Relation avec Progress
    progress = db.relationship('Progress', back_populates='exercise', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Exercise {self.number}>' 