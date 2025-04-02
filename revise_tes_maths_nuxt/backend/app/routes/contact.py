from flask import Blueprint, request, jsonify
from app.models.contact_message import ContactMessage
from app import db
from flask_login import login_required
from app.routes.admin import admin_required

bp = Blueprint('contact', __name__)

@bp.route('/api/contact', methods=['POST'])
def submit_contact():
    """Enregistrer un nouveau message de contact"""
    data = request.get_json()
    
    if not all(key in data for key in ['name', 'email', 'message']):
        return jsonify({'error': 'Nom, email et message sont requis'}), 400
        
    message = ContactMessage(
        name=data['name'],
        email=data['email'],
        phone=data.get('phone'),  # Optionnel
        message=data['message']
    )
    
    try:
        db.session.add(message)
        db.session.commit()
        return jsonify({'message': 'Message envoyé avec succès'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erreur lors de l\'envoi du message'}), 500

@bp.route('/api/admin/contact-messages', methods=['GET'])
@login_required
@admin_required
def get_contact_messages():
    """Récupérer tous les messages de contact (admin seulement)"""
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return jsonify([{
        'id': msg.id,
        'name': msg.name,
        'email': msg.email,
        'phone': msg.phone,
        'message': msg.message,
        'created_at': msg.created_at.isoformat(),
        'is_read': msg.is_read
    } for msg in messages])

@bp.route('/api/admin/contact-messages/<int:id>/mark-as-read', methods=['PUT'])
@login_required
@admin_required
def mark_message_as_read(id):
    """Marquer un message comme lu (admin seulement)"""
    message = ContactMessage.query.get_or_404(id)
    message.is_read = True
    db.session.commit()
    return jsonify({'message': 'Message marqué comme lu'})

@bp.route('/api/admin/contact-messages/<int:id>', methods=['DELETE'])
@login_required
@admin_required
def delete_message(id):
    """Supprimer un message (admin seulement)"""
    message = ContactMessage.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'Message supprimé'}) 