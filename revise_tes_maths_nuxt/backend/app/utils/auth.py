from functools import wraps
from flask import jsonify
from flask_login import current_user, login_required as flask_login_required

def admin_required(f):
    """
    Décorateur pour restreindre l'accès aux administrateurs.
    Doit être utilisé après le décorateur login_required.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return jsonify({'error': 'Non autorisé'}), 401
        if not current_user.is_admin:
            return jsonify({'error': 'Accès réservé aux administrateurs'}), 403
        return f(*args, **kwargs)
    return decorated_function

def login_required(f):
    """
    Version modifiée du décorateur login_required de Flask-Login
    qui retourne une réponse JSON au lieu d'une redirection
    """
    @wraps(f)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated:
            return jsonify({'error': 'Non autorisé'}), 401
        return f(*args, **kwargs)
    return decorated_view 