from flask import Blueprint, jsonify, request
from flask_login import login_required
from app import db
from app.models.user import User
from app.utils.auth import admin_required

bp = Blueprint('admin', __name__)

@bp.route('/api/admin/users', methods=['GET'])
@login_required
@admin_required
def get_users():
    """Récupérer la liste des utilisateurs (admin seulement)"""
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_admin': user.is_admin,
        'created_at': user.created_at.isoformat(),
        'last_login': user.last_login.isoformat() if user.last_login else None
    } for user in users])

@bp.route('/api/admin/users/<int:id>', methods=['GET'])
@login_required
@admin_required
def get_user(id):
    """Récupérer les détails d'un utilisateur spécifique (admin seulement)"""
    user = User.query.get_or_404(id)
    return jsonify({
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_admin': user.is_admin,
        'created_at': user.created_at.isoformat()
    })

@bp.route('/api/admin/users/<int:id>', methods=['PUT'])
@login_required
@admin_required
def update_user(id):
    """Mettre à jour un utilisateur (admin seulement)"""
    user = User.query.get_or_404(id)
    data = request.get_json()

    if 'email' in data and data['email'] != user.email:
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Cet email est déjà utilisé'}), 400
        user.email = data['email']

    if 'first_name' in data:
        user.first_name = data['first_name']
    if 'last_name' in data:
        user.last_name = data['last_name']
    if 'is_admin' in data:
        user.is_admin = data['is_admin']
    if 'password' in data:
        user.set_password(data['password'])

    try:
        db.session.commit()
        return jsonify({
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_admin': user.is_admin,
            'created_at': user.created_at.isoformat()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erreur lors de la mise à jour de l\'utilisateur'}), 500

@bp.route('/api/admin/users/<int:id>', methods=['DELETE'])
@login_required
@admin_required
def delete_user(id):
    """Supprimer un utilisateur (admin seulement)"""
    user = User.query.get_or_404(id)
    
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Utilisateur supprimé avec succès'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erreur lors de la suppression de l\'utilisateur'}), 500 