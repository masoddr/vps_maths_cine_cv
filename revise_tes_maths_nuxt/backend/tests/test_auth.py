import json
import pytest
from app.models.user import User

def test_register(client, session):
    """
    GIVEN l'application Flask configurée pour les tests
    WHEN la route '/api/register' est appelée (POST)
    THEN vérifier que l'utilisateur est créé correctement
    """
    data = {
        'email': 'new@example.com',
        'password': 'test123',
        'first_name': 'New',
        'last_name': 'User'
    }
    
    response = client.post(
        '/api/register',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code == 201
    assert response.json['message'] == 'Inscription réussie'
    
    user = User.query.filter_by(email='new@example.com').first()
    assert user is not None
    assert user.first_name == 'New'
    assert user.last_name == 'User'

def test_login_success(client, test_user):
    """
    GIVEN un utilisateur existant
    WHEN la route '/api/login' est appelée avec les bons identifiants
    THEN vérifier que la connexion réussit
    """
    data = {
        'email': 'test@example.com',
        'password': 'password123'
    }
    
    response = client.post(
        '/api/login',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    assert response.json['message'] == 'Connexion réussie'

def test_login_invalid_credentials(client, test_user):
    """
    GIVEN un utilisateur existant
    WHEN la route '/api/login' est appelée avec un mauvais mot de passe
    THEN vérifier que la connexion échoue
    """
    data = {
        'email': 'test@example.com',
        'password': 'wrong_password'
    }
    
    response = client.post(
        '/api/login',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code == 401
    assert b'Email ou mot de passe incorrect' in response.data

def test_logout(client, test_user):
    """
    GIVEN un utilisateur connecté
    WHEN la route '/api/logout' est appelée
    THEN vérifier que la déconnexion réussit
    """
    # D'abord, connectons l'utilisateur
    client.post(
        '/api/login',
        data=json.dumps({
            'email': 'test@example.com',
            'password': 'password123'
        }),
        content_type='application/json'
    )
    
    # Ensuite, testons la déconnexion
    response = client.get('/api/logout')
    assert response.status_code == 200
    assert response.json['message'] == 'Déconnexion réussie' 