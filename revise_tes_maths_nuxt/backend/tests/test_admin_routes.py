import pytest
from app import create_app, db
from app.models.user import User
from flask_login import login_user
import json
from config import TestConfig

@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def admin_user():
    user = User(
        email='admin@test.com',
        first_name='Admin',
        last_name='Test',
        is_admin=True
    )
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def normal_user():
    user = User(
        email='user@test.com',
        first_name='User',
        last_name='Test',
        is_admin=False
    )
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    return user

def login(client, email, password):
    return client.post('/api/login', json={
        'email': email,
        'password': password
    })

def test_get_users_admin(client, admin_user):
    """Test de la récupération de la liste des utilisateurs par un admin"""
    # Connexion en tant qu'admin
    login(client, 'admin@test.com', 'password123')
    
    # Test de la route
    response = client.get('/api/admin/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'email' in data[0]
    assert 'is_admin' in data[0]

def test_get_users_unauthorized(client, normal_user):
    """Test de l'accès non autorisé à la liste des utilisateurs"""
    # Connexion en tant qu'utilisateur normal
    login(client, 'user@test.com', 'password123')
    
    # Test de la route
    response = client.get('/api/admin/users')
    assert response.status_code == 403

def test_get_user_details_admin(client, admin_user, normal_user):
    """Test de la récupération des détails d'un utilisateur par un admin"""
    # Connexion en tant qu'admin
    login(client, 'admin@test.com', 'password123')
    
    # Test de la route
    response = client.get(f'/api/admin/users/{normal_user.id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['email'] == normal_user.email
    assert data['first_name'] == normal_user.first_name
    assert data['last_name'] == normal_user.last_name

def test_update_user_admin(client, admin_user, normal_user):
    """Test de la mise à jour d'un utilisateur par un admin"""
    # Connexion en tant qu'admin
    login(client, 'admin@test.com', 'password123')
    
    # Données de mise à jour
    update_data = {
        'first_name': 'Updated',
        'last_name': 'Name',
        'is_admin': True
    }
    
    # Test de la route
    response = client.put(
        f'/api/admin/users/{normal_user.id}',
        json=update_data
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['first_name'] == update_data['first_name']
    assert data['last_name'] == update_data['last_name']
    assert data['is_admin'] == update_data['is_admin']

def test_delete_user_admin(client, admin_user, normal_user):
    """Test de la suppression d'un utilisateur par un admin"""
    # Connexion en tant qu'admin
    login(client, 'admin@test.com', 'password123')
    
    # Test de la route
    response = client.delete(f'/api/admin/users/{normal_user.id}')
    assert response.status_code == 200
    
    # Vérifier que l'utilisateur a été supprimé
    deleted_user = User.query.get(normal_user.id)
    assert deleted_user is None

def test_update_user_duplicate_email(client, admin_user, normal_user):
    """Test de la mise à jour d'un utilisateur avec un email déjà existant"""
    # Créer un autre utilisateur
    other_user = User(
        email='other@test.com',
        first_name='Other',
        last_name='User'
    )
    other_user.set_password('password123')
    db.session.add(other_user)
    db.session.commit()
    
    # Connexion en tant qu'admin
    login(client, 'admin@test.com', 'password123')
    
    # Essayer de mettre à jour avec un email déjà utilisé
    response = client.put(
        f'/api/admin/users/{normal_user.id}',
        json={'email': 'other@test.com'}
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data 