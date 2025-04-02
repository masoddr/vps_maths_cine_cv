from flask import Blueprint, jsonify, request, send_file, current_app
from app import db
from app.models.exam_paper import ExamPaper
from app.models.exercise import Exercise
from app.utils.auth import admin_required, login_required
from app.utils.storage import save_pdf, delete_pdf
import os
import json

bp = Blueprint('exam_papers', __name__)

@bp.route('/api/exampapers', methods=['GET'])
def get_exam_papers():
    """Récupérer la liste des annales avec filtres optionnels"""
    year = request.args.get('year', type=int)
    query = ExamPaper.query

    if year:
        query = query.filter(ExamPaper.year == year)

    exam_papers = query.all()
    return jsonify([{
        'id': paper.id,
        'title': paper.title,
        'year': paper.year,
        'session': paper.session,
        'level': paper.level,
        'pdf_url': paper.pdf_url,
        'created_at': paper.created_at.isoformat(),
        'updated_at': paper.updated_at.isoformat(),
        'exercises': [{
            'id': exercise.id,
            'number': exercise.number,
            'description': exercise.description,
            'themes': exercise.themes
        } for exercise in paper.exercises]
    } for paper in exam_papers])

@bp.route('/api/exampapers/<int:id>', methods=['GET'])
def get_exam_paper(id):
    """Récupérer les détails d'une annale spécifique"""
    exam_paper = ExamPaper.query.get_or_404(id)
    return jsonify({
        'id': exam_paper.id,
        'title': exam_paper.title,
        'year': exam_paper.year,
        'session': exam_paper.session,
        'level': exam_paper.level,
        'pdf_url': exam_paper.pdf_url,
        'created_at': exam_paper.created_at.isoformat(),
        'updated_at': exam_paper.updated_at.isoformat(),
        'exercises': [{
            'id': exercise.id,
            'number': exercise.number,
            'description': exercise.description,
            'themes': exercise.themes
        } for exercise in exam_paper.exercises]
    })

@bp.route('/api/exampapers', methods=['POST'])
@admin_required
def create_exam_paper():
    """Créer une nouvelle annale (admin seulement)"""
    try:
        # Vérifier les données du formulaire
        data = request.form
        if 'title' not in data:
            return jsonify({'error': 'Le titre est requis'}), 400
        if 'year' not in data:
            return jsonify({'error': 'L\'année est requise'}), 400
        if 'exercises' not in data:
            return jsonify({'error': 'Les exercices sont requis'}), 400
        
        # Vérifier si un PDF a été fourni
        if 'pdf' not in request.files:
            return jsonify({'error': 'Le PDF est requis'}), 400
            
        pdf_file = request.files['pdf']
        if not pdf_file:
            return jsonify({'error': 'Le PDF est requis'}), 400
            
        # Sauvegarder le PDF
        try:
            pdf_url = save_pdf(pdf_file)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
        exam_paper = ExamPaper(
            title=data['title'],
            year=int(data['year']),
            pdf_url=pdf_url
        )
        
        # Ajouter les exercices
        exercises_data = json.loads(data['exercises'])
        for exercise_data in exercises_data:
            if 'themes' not in exercise_data:
                raise ValueError('Les thèmes de l\'exercice sont requis')
            if not exercise_data['themes']:
                raise ValueError('Au moins un thème doit être sélectionné pour chaque exercice')
                
            exercise = Exercise(
                number=exercise_data['number'],
                themes=exercise_data['themes'],
                exam_paper=exam_paper
            )
            db.session.add(exercise)
        
        db.session.add(exam_paper)
        db.session.commit()
        
        return jsonify({
            'id': exam_paper.id,
            'title': exam_paper.title,
            'year': exam_paper.year,
            'pdf_url': exam_paper.pdf_url,
            'exercises': [{
                'id': exercise.id,
                'number': exercise.number,
                'themes': exercise.themes
            } for exercise in exam_paper.exercises]
        }), 201
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f"Erreur détaillée lors de la création de l'annale: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Erreur lors de la création de l\'annale: {str(e)}'}), 500

@bp.route('/api/exampapers/<int:id>', methods=['PUT'])
@admin_required
def update_exam_paper(id):
    """Mettre à jour une annale existante (admin seulement)"""
    exam_paper = ExamPaper.query.get_or_404(id)
    old_pdf_url = exam_paper.pdf_url
    
    try:
        # Mise à jour du PDF si fourni
        if 'pdf' in request.files and request.files['pdf']:
            pdf_file = request.files['pdf']
            if pdf_file:
                # Supprimer l'ancien PDF
                if old_pdf_url:
                    try:
                        delete_pdf(old_pdf_url)
                    except Exception:
                        pass  # Ignorer les erreurs de suppression
                
                # Sauvegarder le nouveau PDF
                pdf_url = save_pdf(pdf_file)
                exam_paper.pdf_url = pdf_url
        
        # Mise à jour des autres champs
        data = request.form
        if 'title' in data:
            exam_paper.title = data['title']
        if 'year' in data:
            exam_paper.year = int(data['year'])
        
        db.session.commit()
        
        return jsonify({
            'id': exam_paper.id,
            'title': exam_paper.title,
            'year': exam_paper.year,
            'pdf_url': exam_paper.pdf_url,
            'created_at': exam_paper.created_at.isoformat(),
            'updated_at': exam_paper.updated_at.isoformat()
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # En cas d'erreur, restaurer l'ancien PDF
        exam_paper.pdf_url = old_pdf_url
        db.session.rollback()
        return jsonify({'error': 'Erreur lors de la mise à jour de l\'annale'}), 500

@bp.route('/api/exampapers/<int:id>', methods=['DELETE'])
@admin_required
def delete_exam_paper(id):
    """Supprimer une annale (admin seulement)"""
    exam_paper = ExamPaper.query.get_or_404(id)
    
    try:
        # Supprimer le fichier PDF
        if exam_paper.pdf_url:
            delete_pdf(exam_paper.pdf_url)
        
        # Supprimer l'entrée de la base de données
        db.session.delete(exam_paper)
        db.session.commit()
        
        return jsonify({'message': 'Annale supprimée avec succès'})
        
    except Exception as e:
        return jsonify({'error': 'Erreur lors de la suppression de l\'annale'}), 500

@bp.route('/api/exampapers/<int:id>/pdf', methods=['GET'])
def download_exam_paper_pdf(id):
    """Télécharger le PDF d'une annale"""
    exam_paper = ExamPaper.query.get_or_404(id)
    
    if not exam_paper.pdf_url:
        return jsonify({'error': 'Aucun PDF disponible pour cette annale'}), 404
        
    try:
        # Vérifier si le fichier existe
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'pdfs', os.path.basename(exam_paper.pdf_url))
        
        if not os.path.exists(file_path):
            return jsonify({'error': 'Le fichier PDF est introuvable'}), 404
        
        # Servir le fichier directement
        return send_file(
            file_path,
            mimetype='application/pdf',
            as_attachment=False  # Pour afficher dans le navigateur au lieu de télécharger
        )
    except Exception as e:
        return jsonify({'error': 'Erreur lors du téléchargement du PDF'}), 500 