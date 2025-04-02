from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from app import db
from datetime import datetime, UTC
import requests

bp = Blueprint('auth', __name__)

@bp.route('/api/auth/me')
@login_required
def me():
    """Récupérer les informations de l'utilisateur connecté"""
    return jsonify({
        'user': {
            'id': current_user.id,
            'email': current_user.email,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'is_admin': current_user.is_admin,
            'updated_at': current_user.updated_at.isoformat() if current_user.updated_at else None
        }
    })

@bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Cet email est déjà utilisé'}), 400
        
    user = User(
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name']
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    # Envoyer une notification ntfy
    try:
        message = f"Nouvel utilisateur inscrit : {user.first_name} {user.last_name} ({user.email})"
        requests.post('https://ntfy.sh/nouvel_utilisateur_revise_tes_maths', 
                     data=message.encode(encoding='utf-8'))
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification ntfy : {e}")
    
    return jsonify({'message': 'Inscription réussie'}), 201

@bp.route('/api/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify({'error': 'Déjà connecté'}), 400
        
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user is None or not user.check_password(data['password']):
        return jsonify({'error': 'Email ou mot de passe incorrect'}), 401
        
    login_user(user)
    user.last_login = datetime.now(UTC)
    db.session.commit()
    
    return jsonify({
        'message': 'Connexion réussie',
        'user': {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_admin': user.is_admin
        }
    })

@bp.route('/api/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Déconnexion réussie'}) 