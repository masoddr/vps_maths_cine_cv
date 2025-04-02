import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'postgresql://revise_tes_maths:revise_tes_maths@localhost/revise_tes_maths_test'
    })
    
    return app

@pytest.fixture(scope='session')
def _db(app):
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def session(_db, app):
    with app.app_context():
        connection = _db.engine.connect()
        transaction = connection.begin()
        
        session = db.session
        session.begin_nested()
        
        # Nettoyer toutes les tables avant chaque test
        for table in reversed(_db.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()
        
        yield session
        
        session.close()
        transaction.rollback()
        connection.close()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_user(session):
    user = User(
        email='test@example.com',
        first_name='Test',
        last_name='User'
    )
    user.set_password('password123')
    session.add(user)
    session.commit()
    return user 