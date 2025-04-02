from app import create_app, db
from app.models.user import User

app = create_app()
with app.app_context():
    # Vérifier si l'admin existe déjà
    existing_admin = User.query.filter_by(email='admin@example.com').first()
    if existing_admin is None:
        # Créer un utilisateur administrateur
        admin = User(
            email='admin@example.com',
            first_name='Admin',
            last_name='User',
            is_admin=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print('Administrateur créé avec succès !')
    else:
        print('L\'administrateur existe déjà.') 