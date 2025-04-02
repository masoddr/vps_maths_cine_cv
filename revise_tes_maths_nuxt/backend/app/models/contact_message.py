from datetime import datetime, UTC
from app import db

class ContactMessage(db.Model):
    """Modèle représentant un message de contact"""
    
    __tablename__ = 'contact_message'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
    is_read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<ContactMessage from {self.name} ({self.email})>' 