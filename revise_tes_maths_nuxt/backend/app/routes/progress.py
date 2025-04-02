from flask import Blueprint, request, jsonify, abort
from flask_login import login_required, current_user
from app import db
from app.models.progress import Progress
from app.models.exercise import Exercise

bp = Blueprint('progress', __name__)

@bp.route('/api/progress', methods=['GET'])
@login_required
def get_progress():
    """Récupérer la progression de l'élève connecté"""
    progress_list = Progress.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': p.id,
        'exercise_id': p.exercise_id,
        'status': p.status,
        'time_spent': p.time_spent,
        'notes': p.notes,
        'updated_at': p.updated_at.isoformat() if p.updated_at else None,
        'title': f'Exercice {p.exercise.number}',
        'description': p.exercise.description,
        'themes': p.exercise.themes,
        'examPaper': p.exercise.exam_paper.title if p.exercise.exam_paper else None
    } for p in progress_list])

@bp.route('/api/progress/<int:exercise_id>', methods=['POST', 'PUT'])
@login_required
def create_or_update_progress(exercise_id):
    """Créer ou mettre à jour la progression sur un exercice"""
    data = request.get_json()
    
    # Vérifier que l'exercice existe
    exercise = db.session.get(Exercise, exercise_id)
    if exercise is None:
        abort(404)
    
    # Vérifier que le statut est valide
    if 'status' in data and data['status'] not in Progress.VALID_STATUSES:
        return jsonify({
            'error': f"Statut invalide. Doit être l'un des suivants : {', '.join(Progress.VALID_STATUSES)}"
        }), 400
    
    # Rechercher une progression existante ou en créer une nouvelle
    progress = Progress.query.filter_by(
        user_id=current_user.id,
        exercise_id=exercise_id
    ).first()
    
    if progress:
        # Mise à jour de la progression existante
        if 'status' in data:
            progress.status = data['status']
        if 'time_spent' in data:
            progress.time_spent = data['time_spent']
        if 'notes' in data:
            progress.notes = data['notes']
    else:
        # Création d'une nouvelle progression
        progress = Progress(
            user_id=current_user.id,
            exercise_id=exercise_id,
            status=data.get('status', 'not_started'),
            time_spent=data.get('time_spent'),
            notes=data.get('notes')
        )
        db.session.add(progress)
    
    db.session.commit()
    
    return jsonify({
        'id': progress.id,
        'exercise_id': progress.exercise_id,
        'status': progress.status,
        'time_spent': progress.time_spent,
        'notes': progress.notes,
        'updated_at': progress.updated_at.isoformat() if progress.updated_at else None
    })

@bp.route('/api/progress/stats', methods=['GET'])
@login_required
def get_progress_stats():
    """Récupérer les statistiques de progression de l'élève"""
    # Récupérer tous les exercices et les progrès
    total_exercises = Exercise.query.count()
    user_progress = Progress.query.filter_by(user_id=current_user.id).all()
    
    # Statistiques de base
    completed_exercises = sum(1 for p in user_progress if p.status == 'completed')
    in_progress = sum(1 for p in user_progress if p.status == 'in_progress')
    
    # Calcul du temps total (en heures)
    total_hours = sum(p.time_spent or 0 for p in user_progress) / 60 if user_progress else 0
    
    # Calcul des thèmes maîtrisés
    themes_progress = {}
    for progress in user_progress:
        if progress.status == 'completed':
            for theme in progress.exercise.themes:
                if theme not in themes_progress:
                    themes_progress[theme] = {'total': 0, 'completed': 0}
                themes_progress[theme]['completed'] += 1
        # Compter le total d'exercices par thème
        for theme in progress.exercise.themes:
            if theme not in themes_progress:
                themes_progress[theme] = {'total': 0, 'completed': 0}
            themes_progress[theme]['total'] += 1
    
    # Compter les thèmes maîtrisés (plus de 80% de réussite)
    mastered_themes = sum(
        1 for stats in themes_progress.values()
        if stats['total'] > 0 and (stats['completed'] / stats['total']) >= 0.8
    )
    
    # Calculer le pourcentage global de progression
    global_progress = (completed_exercises / total_exercises * 100) if total_exercises > 0 else 0
    
    stats = {
        'global': round(global_progress, 1),
        'completedExercises': completed_exercises,
        'totalExercises': total_exercises,
        'inProgress': in_progress,
        'totalHours': round(total_hours, 1),
        'masteredTopics': mastered_themes,
        'totalTopics': len(themes_progress),
        'themesProgress': {
            theme: {
                'completed': stats['completed'],
                'total': stats['total'],
                'percentage': (stats['completed'] / stats['total'] * 100) if stats['total'] > 0 else 0
            }
            for theme, stats in themes_progress.items()
        }
    }
    
    return jsonify(stats)

@bp.route('/api/progress/exercises', methods=['GET'])
@login_required
def get_exercises_with_progress():
    """Récupérer les exercices avec leur progression"""
    progress_list = Progress.query.filter_by(user_id=current_user.id).all()
    
    exercises_with_progress = []
    for progress in progress_list:
        exercise = progress.exercise
        exercises_with_progress.append({
            'id': exercise.id,
            'exercise_id': exercise.id,
            'number': exercise.number,
            'title': f'Exercice {exercise.number}',
            'description': exercise.description,
            'themes': exercise.themes,
            'status': progress.status,
            'notes': progress.notes,
            'examPaper': exercise.exam_paper.title if exercise.exam_paper else None,
            'updated_at': progress.updated_at.isoformat() if progress.updated_at else None
        })
    
    return jsonify(exercises_with_progress) 