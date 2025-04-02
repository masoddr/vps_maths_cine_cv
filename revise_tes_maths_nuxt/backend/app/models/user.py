from datetime import datetime, UTC
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    """Modèle représentant un utilisateur"""
    
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))
    last_login = db.Column(db.DateTime, nullable=True)

    # Relation avec Progress
    progress = db.relationship('Progress', back_populates='user', cascade='all, delete-orphan')

    def set_password(self, password):
        """Définir le mot de passe de l'utilisateur"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Vérifier le mot de passe de l'utilisateur"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'

@login.user_loader
def load_user(id):
    """Charger un utilisateur depuis la base de données"""
    return db.session.get(User, int(id)) 