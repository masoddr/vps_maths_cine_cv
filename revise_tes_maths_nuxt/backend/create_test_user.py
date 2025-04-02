from app import create_app, db
from app.models.user import User

app = create_app()
with app.app_context():
    # Créer un utilisateur de test
    user = User(
        email='test@example.com',
        first_name='Test',
        last_name='User'
    )
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    print('Utilisateur de test créé avec succès !') 