from flask import Blueprint, jsonify
from flask_login import login_required

bp = Blueprint('main', __name__)

@bp.route('/api/test')
def test():
    return jsonify({'message': 'API opérationnelle !'})

@bp.route('/api/protected')
@login_required
def protected():
    return jsonify({'message': 'Vous êtes connecté et pouvez accéder à cette ressource.'}) 