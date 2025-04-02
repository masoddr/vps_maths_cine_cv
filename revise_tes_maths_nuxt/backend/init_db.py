from app import create_app, db
from app.models.user import User
from app.models.exam_paper import ExamPaper
from app.models.exercise import Exercise
from app.models.progress import Progress

app = create_app()

with app.app_context():
    # Créer toutes les tables
    db.drop_all()
    db.create_all()
    
    # Créer un utilisateur administrateur
    admin = User(
        email='admin@example.com',
        first_name='Admin',
        last_name='User',
        is_admin=True
    )
    admin.set_password('admin123')
    db.session.add(admin)
    
    # Créer un exemple d'annale
    exam = ExamPaper(
        title='Bac S 2023 - Session Normale',
        year=2023,
        session='normale',
        level='terminale'
    )
    db.session.add(exam)
    
    # Créer quelques exercices
    exercise1 = Exercise(
        number=1,
        description='Exercice sur les fonctions exponentielles',
        themes=['fonctions', 'exponentielle'],
        exam_paper=exam
    )
    db.session.add(exercise1)
    
    # Sauvegarder les changements
    db.session.commit()
    
    print('Base de données initialisée avec succès !') 