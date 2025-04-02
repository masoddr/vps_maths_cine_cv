import os
from werkzeug.utils import secure_filename
from flask import current_app
import uuid
import logging
import mimetypes

logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = {'pdf'}
ALLOWED_MIMETYPES = {'application/pdf'}

def allowed_file(filename):
    """Vérifie si l'extension du fichier est autorisée"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_unique_filename(filename):
    """Génère un nom de fichier unique"""
    ext = filename.rsplit('.', 1)[1].lower()
    return f"{uuid.uuid4()}.{ext}"

def save_pdf(pdf_file):
    """Sauvegarder un fichier PDF dans le dossier de stockage"""
    try:
        if not pdf_file or not allowed_file(pdf_file.filename):
            raise ValueError("Type de fichier non autorisé")

        # Vérifier le type MIME
        mime_type = pdf_file.content_type
        if mime_type not in ALLOWED_MIMETYPES:
            raise ValueError(f"Type MIME non autorisé : {mime_type}")

        # Créer le dossier de stockage s'il n'existe pas
        upload_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], 'pdfs')
        os.makedirs(upload_dir, exist_ok=True)
        
        # Générer un nom de fichier unique
        unique_filename = f"{uuid.uuid4()}.pdf"
        final_filepath = os.path.join(upload_dir, unique_filename)
        
        # Sauvegarder le fichier en mode binaire
        pdf_file.save(final_filepath)
        
        # Vérifier que le fichier a été correctement sauvegardé
        if not os.path.exists(final_filepath):
            raise ValueError("Erreur lors de la sauvegarde du fichier")
            
        # Vérifier la taille du fichier
        if os.path.getsize(final_filepath) == 0:
            os.remove(final_filepath)
            raise ValueError("Le fichier sauvegardé est vide")
        
        logger.info(f"PDF sauvegardé avec succès : {final_filepath}")
        return f'/static/uploads/pdfs/{unique_filename}'
        
    except Exception as e:
        logger.error(f"Erreur lors de la sauvegarde du PDF : {e}")
        # Si un fichier a été créé mais est invalide, le supprimer
        if 'final_filepath' in locals() and os.path.exists(final_filepath):
            os.remove(final_filepath)
        raise ValueError(f"Erreur lors de la sauvegarde du PDF : {str(e)}")

def delete_pdf(pdf_url):
    """
    Supprime un fichier PDF
    
    Args:
        pdf_url: L'URL relative du fichier à supprimer
        
    Returns:
        bool: True si le fichier a été supprimé, False sinon
    """
    if not pdf_url or not pdf_url.startswith('/static/uploads/pdfs/'):
        return False
    
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'pdfs', os.path.basename(pdf_url))
    
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.info(f"PDF supprimé : {file_path}")
            return True
    except Exception as e:
        logger.error(f"Erreur lors de la suppression du PDF : {str(e)}")
        
    return False 