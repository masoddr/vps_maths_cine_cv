import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://revise_tes_maths:revise_tes_maths@localhost/revise_tes_maths_test'
    app.config['TESTING'] = True
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_new_user():
    """
    GIVEN un modèle User
    WHEN un nouvel utilisateur est créé
    THEN vérifier que l'email et le mot de passe sont définis correctement
    """
    user = User(email='test@test.com')
    user.set_password('test123')
    assert user.email == 'test@test.com'
    assert user.password_hash != 'test123'
    assert user.check_password('test123')
    assert not user.check_password('wrong_password')

def test_user_representation():
    """
    GIVEN un modèle User
    WHEN on affiche l'utilisateur
    THEN vérifier que la représentation est correcte
    """
    user = User(email='test@test.com')
    assert str(user) == '<User test@test.com>' 