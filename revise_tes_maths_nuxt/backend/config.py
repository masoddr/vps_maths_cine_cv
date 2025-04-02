import os
from dotenv import load_dotenv
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config:
    # Configuration générale
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-very-secret'
    
    # Configuration de la base de données
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuration du serveur
    DEBUG = os.environ.get('FLASK_DEBUG', '0') == '1'
    
    # Configuration des uploads
    UPLOAD_FOLDER = os.path.join(basedir, 'app/static/uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max-limit
    
    # Configuration de session
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)
    
    # Configuration CORS
    CORS_HEADERS = 'Content-Type'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False 