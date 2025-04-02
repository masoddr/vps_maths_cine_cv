import pytest
from app import create_app, db
from config import TestConfig

@pytest.fixture(scope='session')
def app():
    app = create_app(TestConfig)
    return app

@pytest.fixture(scope='session')
def _db(app):
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()

@pytest.fixture(scope='function')
def session(_db, app):
    with app.app_context():
        connection = _db.engine.connect()
        transaction = connection.begin()
        session = _db.session
        session.begin_nested()

        # Supprime toutes les données des tables
        for table in reversed(_db.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()

        yield session
        session.close()
        transaction.rollback()
        connection.close() 