from flask import Flask, send_from_directory, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from config import Config
import os
from datetime import timedelta
from flask import Blueprint
from flask_login import login_required

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

bp = Blueprint('main', __name__)

@bp.route('/api/test')
def test():
    return jsonify({'message': 'API opérationnelle !'})

@bp.route('/api/protected')
@login_required
def protected():
    return jsonify({'message': 'Vous êtes connecté et pouvez accéder à cette ressource.'})

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Configuration des sessions
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'
    app.config['SESSION_COOKIE_NAME'] = 'rtm_session'
    app.config['SESSION_COOKIE_DOMAIN'] = 'revise-tes-maths.fr'
    
    # Configuration du dossier de stockage
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(app.root_path), 'static', 'uploads')
    
    # Configuration CORS plus permissive
    CORS(app, 
         resources={r"/api/*": {
             "origins": [
                 "https://revise-tes-maths.fr",
                 "https://www.revise-tes-maths.fr",
                 "http://revise-tes-maths.fr",
                 "http://www.revise-tes-maths.fr"
             ],
             "supports_credentials": True,
             "allow_headers": ["Content-Type", "Authorization", "Cookie"],
             "expose_headers": ["Content-Range", "X-Content-Range", "Set-Cookie"],
             "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
             "max_age": 3600
         }})
    
    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    
    # Ajout d'un middleware pour logger les requêtes
    @app.before_request
    def log_request_info():
        app.logger.debug('Headers: %s', request.headers)
        app.logger.debug('Body: %s', request.get_data())

    # Ajout d'un middleware pour logger les réponses
    @app.after_request
    def after_request(response):
        app.logger.debug('Response Headers: %s', response.headers)
        return response
    
    # Configurer le gestionnaire de connexion
    login.login_view = None  # Désactiver la redirection
    login.login_message = 'Veuillez vous connecter pour accéder à cette page.'
    login.session_protection = 'strong'
    
    # Gestionnaire d'erreur pour les requêtes non authentifiées
    @login.unauthorized_handler
    def unauthorized():
        return jsonify({'error': 'Non autorisé'}), 401
    
    # Créer les dossiers de stockage s'ils n'existent pas
    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'pdfs'), exist_ok=True)
    
    # Route pour servir les fichiers statiques
    @app.route('/static/uploads/pdfs/<filename>')
    def serve_pdf(filename):
        return send_from_directory(
            os.path.join(app.config['UPLOAD_FOLDER'], 'pdfs'),
            filename,
            mimetype='application/pdf'
        )
    
    # Importer les modèles
    from app.models.user import User
    from app.models.exam_paper import ExamPaper
    from app.models.exercise import Exercise
    from app.models.progress import Progress
    from app.models.contact_message import ContactMessage
    
    # Enregistrer les blueprints
    from app.routes import auth, exam_papers, progress, admin, contact
    app.register_blueprint(auth.bp)
    app.register_blueprint(exam_papers.bp)
    app.register_blueprint(progress.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(contact.bp)
    app.register_blueprint(bp)  # Enregistrement du blueprint main
    
    # Health check route
    @app.route('/api/health')
    def health_check():
        return jsonify({
            'status': 'healthy',
            'service': 'rtm-backend'
        })
    
    return app 