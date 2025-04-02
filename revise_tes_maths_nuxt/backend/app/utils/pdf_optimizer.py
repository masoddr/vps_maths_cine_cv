import os
import subprocess
from flask import current_app
import logging

logger = logging.getLogger(__name__)

def optimize_pdf(input_path, output_path=None):
    """
    Optimise un fichier PDF en utilisant Ghostscript.
    Réduit la taille du fichier tout en maintenant une qualité acceptable.
    
    Args:
        input_path: Chemin du fichier PDF d'entrée
        output_path: Chemin du fichier PDF de sortie (optionnel)
        
    Returns:
        str: Chemin du fichier PDF optimisé
    """
    if output_path is None:
        filename, ext = os.path.splitext(input_path)
        output_path = f"{filename}_optimized{ext}"

    try:
        # Vérifier si Ghostscript est installé
        subprocess.run(['gs', '--version'], capture_output=True, check=True)
        
        # Paramètres d'optimisation
        gs_params = [
            'gs',
            '-sDEVICE=pdfwrite',
            '-dCompatibilityLevel=1.4',
            '-dPDFSETTINGS=/ebook',  # Qualité ebook (taille moyenne)
            '-dNOPAUSE',
            '-dQUIET',
            '-dBATCH',
            f'-sOutputFile={output_path}',
            input_path
        ]
        
        # Exécuter Ghostscript
        result = subprocess.run(gs_params, capture_output=True, check=True)
        
        if result.returncode == 0:
            # Vérifier si l'optimisation a réduit la taille
            original_size = os.path.getsize(input_path)
            optimized_size = os.path.getsize(output_path)
            
            if optimized_size < original_size:
                logger.info(f"PDF optimisé : {original_size} -> {optimized_size} bytes")
                return output_path
            else:
                # Si pas d'amélioration, utiliser l'original
                os.remove(output_path)
                return input_path
                
    except subprocess.CalledProcessError as e:
        logger.error(f"Erreur lors de l'optimisation du PDF : {str(e)}")
        return input_path
    except Exception as e:
        logger.error(f"Erreur inattendue lors de l'optimisation : {str(e)}")
        return input_path

def get_compression_settings(file_size):
    """
    Retourne les paramètres de compression appropriés en fonction de la taille du fichier.
    
    Args:
        file_size: Taille du fichier en bytes
        
    Returns:
        str: Paramètre PDFSETTINGS pour Ghostscript
    """
    MB = 1024 * 1024
    
    if file_size > 10 * MB:
        return '/ebook'  # Compression moyenne
    elif file_size > 5 * MB:
        return '/printer'  # Compression légère
    else:
        return '/prepress'  # Qualité maximale 