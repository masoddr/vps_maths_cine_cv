from app import create_app, db
from app.models.user import User
from app.models.exam_paper import ExamPaper
from app.models.exercise import Exercise
from app.models.progress import Progress
from werkzeug.security import generate_password_hash
from datetime import datetime, UTC
import json

def seed_database():
    """Remplir la base de données avec des données de test"""
    app = create_app()
    
    with app.app_context():
        print("Suppression des données existantes...")
        Progress.query.delete()
        Exercise.query.delete()
        ExamPaper.query.delete()
        User.query.delete()
        
        print("Création des utilisateurs...")
        admin = User(
            email='admin@example.com',
            first_name='Admin',
            last_name='User',
            is_admin=True
        )
        admin.set_password('admin123')
        
        user = User(
            email='user@example.com',
            password_hash=generate_password_hash('userpass'),
            first_name='Regular',
            last_name='User',
            is_admin=False
        )
        
        db.session.add(admin)
        db.session.add(user)
        
        print("Création des annales...")
        exam_paper1 = ExamPaper(
            title='Bac 2024 - Amérique du Nord',
            year=2024,
            pdf_url='/static/uploads/pdfs/bac2024_amerique_nord.pdf'
        )
        
        exam_paper2 = ExamPaper(
            title='Bac 2024 - Métropole',
            year=2024,
            pdf_url='/static/uploads/pdfs/bac2024_metropole.pdf'
        )
        
        db.session.add(exam_paper1)
        db.session.add(exam_paper2)
        
        print("Création des exercices...")
        exercises1 = [
            Exercise(
                number=1,
                description='Probabilités et suites numériques',
                themes=['Probabilités', 'Suites numériques'],
                exam_paper=exam_paper1
            ),
            Exercise(
                number=2,
                description='Géométrie dans l\'espace',
                themes=['Géométrie dans l\'espace'],
                exam_paper=exam_paper1
            ),
            Exercise(
                number=3,
                description='Fonction exponentielle',
                themes=['Fonctions', 'Logarithmes'],
                exam_paper=exam_paper1
            ),
            Exercise(
                number=4,
                description='Algorithme Python',
                themes=['Python', 'Suites numériques'],
                exam_paper=exam_paper1
            )
        ]
        
        exercises2 = [
            Exercise(
                number=1,
                description='Équations différentielles',
                themes=['Équations différentielles'],
                exam_paper=exam_paper2
            ),
            Exercise(
                number=2,
                description='Primitives et calcul intégral',
                themes=['Primitives'],
                exam_paper=exam_paper2
            ),
            Exercise(
                number=3,
                description='Nombres complexes',
                themes=['Nombres complexes'],
                exam_paper=exam_paper2
            ),
            Exercise(
                number=4,
                description='Probabilités conditionnelles',
                themes=['Probabilités'],
                exam_paper=exam_paper2
            )
        ]
        
        for exercise in exercises1 + exercises2:
            db.session.add(exercise)
        
        print("Création des progrès...")
        progress1 = Progress(
            user=user,
            exercise=exercises1[0],
            status='completed'
        )
        
        progress2 = Progress(
            user=user,
            exercise=exercises1[1],
            status='in_progress'
        )
        
        db.session.add(progress1)
        db.session.add(progress2)
        
        print("Sauvegarde des changements...")
        db.session.commit()
        print("Base de données initialisée avec succès!")

if __name__ == '__main__':
    seed_database() 