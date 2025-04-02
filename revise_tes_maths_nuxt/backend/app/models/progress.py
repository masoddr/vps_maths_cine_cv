from datetime import datetime, UTC
from app import db

class Progress(db.Model):
    """Modèle représentant la progression d'un utilisateur sur un exercice"""
    
    __tablename__ = 'progress'

    VALID_STATUSES = ['not_started', 'in_progress', 'completed']

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(32), nullable=False, default='not_started')
    time_spent = db.Column(db.Integer)  # temps passé en minutes
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    # Clés étrangères
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)

    # Relations
    user = db.relationship('User', back_populates='progress')
    exercise = db.relationship('Exercise', back_populates='progress')

    def __init__(self, **kwargs):
        if 'status' in kwargs and kwargs['status'] not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status. Must be one of: {', '.join(self.VALID_STATUSES)}")
        super(Progress, self).__init__(**kwargs)

    def __repr__(self):
        return f'<Progress User: {self.user.email}, Exercise: {self.exercise.number}, Status: {self.status}>' 