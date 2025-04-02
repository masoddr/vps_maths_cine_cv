from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import fitz  # PyMuPDF
from typing import Optional, List, Dict, Union, Any
import os
from dotenv import load_dotenv
import json
from openai import OpenAI
import logging
from httpx import HTTPStatusError
import re

# Chargement des variables d'environnement
load_dotenv()

# Vérification de la présence de la clé API
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")

# Initialisation du client OpenAI avec l'API Groq
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Configuration des logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Configuration CORS plus détaillée avec logs
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",  # Ajout de votre port 3001
    "http://127.0.0.1:3001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CVAnalysisResponse(BaseModel):
    hasTitle: bool
    titleFeedback: str
    hasGoodStructure: bool
    structureFeedback: str
    topKeywords: List[str]
    presentKeywords: List[str]
    missingKeywords: List[str]
    keywordSuggestions: Dict[str, List[str]]
    alerts: List[str]
    contentFeedback: Dict[str, List[str]]
    optimizedVersion: str
    scores: Dict[str, float]
    totalScore: float
    jobMatch: Optional[Dict[str, Union[float, List[str]]]] = None

    class Config:
        arbitrary_types_allowed = True

@app.post("/analyze-cv", response_model=CVAnalysisResponse)
async def analyze_cv(
    request: Request,
    file: Optional[UploadFile] = File(None),
    cv_content: Optional[str] = Form(None),
    job_offer: Optional[str] = Form(None)
):
    logger.info(f"Requête reçue - Origin: {request.headers.get('origin')}")
    logger.info(f"Headers reçus: {request.headers}")
    
    # Récupération du contenu du CV
    if file:
        # Lecture du PDF
        pdf_bytes = await file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        cv_text = ""
        for page in doc:
            cv_text += page.get_text()
    else:
        cv_text = cv_content if cv_content else ""

    if not cv_text.strip():
        raise HTTPException(status_code=400, detail="CV content is required")

    # Construction du prompt en plusieurs parties
    compatibility_text = ' et sa compatibilité avec l\'offre d\'emploi' if job_offer else ''
    prompt_header = f"Tu es un expert ATS qui analyse les CV. Fais une analyse approfondie de ce CV{compatibility_text}.\n\n"
    prompt_header += "CV à analyser :\n"
    prompt_header += cv_text + "\n\n"
    
    if job_offer:
        prompt_header += "Offre d'emploi à analyser :\n"
        prompt_header += job_offer + "\n\n"

    prompt_instructions = """Réalise l'analyse suivante :

1. MOTS-CLÉS (40 mots-clés essentiels)
   - Liste les 40 mots-clés les plus importants pour ce type de poste
   - Identifie ceux présents dans le CV
   - Identifie ceux manquants
   - Suggère des formulations alternatives pour les mots-clés manquants

2. STRUCTURE ET FORMAT
   - Vérifie la présence et la clarté du titre
   - Analyse la hiérarchie des sections
   - Vérifie la cohérence du formatage
   - Identifie les éventuels problèmes de mise en page

3. LISIBILITÉ ATS
   - Détecte les abréviations à expliciter
   - Identifie les éléments potentiellement illisibles
   - Vérifie la compatibilité du format avec les ATS

4. CONTENU ET IMPACT
   - Évalue la pertinence des expériences décrites
   - Vérifie la présence de résultats quantifiables
   - Analyse l'utilisation de verbes d'action
   - Identifie les réalisations clés"""

    prompt_compatibility = """5. ANALYSE DÉTAILLÉE DE COMPATIBILITÉ AVEC L'OFFRE
    - Calcule un score précis de correspondance technique en comparant les technologies et compétences requises
    - Évalue le niveau d'expérience demandé vs celui du candidat
    - Analyse la correspondance des soft skills mentionnés dans l'offre
    - Identifie précisément :
        * Les points forts qui correspondent exactement aux besoins
        * Les écarts spécifiques entre le profil et les exigences
        * Des recommandations concrètes basées sur les écarts identifiés
    - Calcule des scores de compatibilité en pourcentage pour chaque aspect
    
    Les scores doivent être calculés ainsi :
    - Score technique : % des compétences techniques requises présentes dans le CV
    - Score expérience : % de correspondance entre l'expérience demandée et celle du candidat
    - Score soft skills : % des soft skills requis présents dans le CV
    - Score global : moyenne pondérée des trois scores précédents""" if job_offer else "5. NOTATION DÉTAILLÉE"

    prompt_important = """
IMPORTANT : 
- Le score total doit être sur 20 points maximum
- Chaque score individuel doit être sur 5 points maximum
- Les scores de compatibilité doivent être en pourcentage (0-100%)"""

    response_format = {
        "hasTitle": True,
        "titleFeedback": "Le titre est clair et bien visible",
        "hasGoodStructure": True,
        "structureFeedback": "La structure est bien organisée",
        "topKeywords": ["mot1", "mot2", "mot3"],
        "presentKeywords": ["mot1", "mot3"],
        "missingKeywords": ["mot2", "mot4"],
        "keywordSuggestions": {
            "mot_manquant1": ["alternative1", "alternative2"],
            "mot_manquant2": ["alternative1", "alternative2"]
        },
        "alerts": [
            "Attention aux abréviations",
            "Suggestion d'amélioration 1"
        ],
        "contentFeedback": {
            "points_forts": ["point1", "point2", "point3"],
            "points_amelioration": ["suggestion1", "suggestion2"]
        },
        "optimizedVersion": "Version optimisée du CV\n avec des retours à la ligne\n",
        "scores": {
            "titre": 4.5,
            "structure": 4.0,
            "mots_cles": 3.5,
            "lisibilite": 4.0,
            "impact_contenu": 4.2
        },
        "totalScore": 16.0,
        "jobMatch": {
            "score": 0.0,
            "technicalMatch": 0.0,
            "experienceMatch": 0.0,
            "softSkillsMatch": 0.0,
            "strengths": [],
            "gaps": [],
            "recommendations": []
        } if job_offer else None
    }

    # Modification du prompt_format pour être plus explicite
    prompt_format = """
    \nVoici un exemple de la structure JSON attendue (les valeurs sont des exemples, calcule tes propres valeurs basées sur ton analyse) :
    """ + f"\n{json.dumps(response_format, indent=2, ensure_ascii=False)}"

    # Assemblage du prompt final
    prompt = "\n".join([
        prompt_header,
        prompt_instructions,
        prompt_compatibility,
        prompt_important,
        prompt_format
    ])

    try:
        # Appel à l'API via le client OpenAI
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "system",
                "content": """Tu es un expert ATS qui répond uniquement en JSON valide. 
                Pour l'analyse de compatibilité avec l'offre d'emploi :
                - Compare minutieusement chaque exigence de l'offre avec le contenu du CV
                - Calcule tes propres scores précis basés sur la présence réelle des éléments demandés
                - Ne réutilise pas les valeurs d'exemple, fais ta propre analyse détaillée
                - Identifie des écarts concrets et propose des recommandations spécifiques
                - Assure-toi que chaque score et recommandation soit basé sur une analyse réelle du contenu
                La version optimisée du CV doit être une chaîne de caractères avec des retours à la ligne \\n."""
            }, {
                "role": "user",
                "content": prompt
            }],
            temperature=0.7,
            max_tokens=4000
        )

        # Parsing de la réponse
        response_content = completion.choices[0].message.content.strip()
        
        # Debug: afficher la réponse brute
        print("Réponse brute de l'API :", response_content)
        
        # Extraction du JSON de la réponse
        json_match = re.search(r'```json\s*(.*?)\s*```', response_content, re.DOTALL)
        if json_match:
            response_content = json_match.group(1)
        else:
            # Si pas de balises json, on essaie de trouver directement un objet JSON
            json_match = re.search(r'\{.*\}', response_content, re.DOTALL)
            if json_match:
                response_content = json_match.group(0)
        
        response_content = response_content.strip()
        
        try:
            analysis_result = json.loads(response_content)
            
            # Vérification et limitation du score total
            if "totalScore" in analysis_result:
                analysis_result["totalScore"] = min(20.0, float(analysis_result["totalScore"]))
            
            # Vérification des scores individuels
            if "scores" in analysis_result:
                for key in analysis_result["scores"]:
                    analysis_result["scores"][key] = min(5.0, float(analysis_result["scores"][key]))

            # Conversion des scores de compatibilité de décimal à pourcentage
            if job_offer and analysis_result.get("jobMatch"):
                if isinstance(analysis_result["jobMatch"], dict):
                    for key in ["score", "technicalMatch", "experienceMatch", "softSkillsMatch"]:
                        if key in analysis_result["jobMatch"]:
                            # Multiplication par 100 pour convertir en pourcentage
                            value = float(analysis_result["jobMatch"][key]) * 100
                            analysis_result["jobMatch"][key] = min(100.0, value)
                elif isinstance(analysis_result["jobMatch"], (int, float)):
                    # Si jobMatch est un nombre, le convertir en pourcentage
                    score = float(analysis_result["jobMatch"]) * 100
                    analysis_result["jobMatch"] = {
                        "score": min(100.0, score),
                        "technicalMatch": min(100.0, score),
                        "experienceMatch": min(100.0, score),
                        "softSkillsMatch": min(100.0, score),
                        "strengths": [],
                        "gaps": [],
                        "recommendations": []
                    }

            # Autres vérifications...
            if not isinstance(analysis_result["optimizedVersion"], str):
                raise HTTPException(
                    status_code=500,
                    detail="optimizedVersion must be a string"
                )

            logger.info("Analyse du CV réussie")
            return CVAnalysisResponse(**analysis_result)
        except json.JSONDecodeError as e:
            print(f"Contenu de la réponse : {response_content}")
            raise HTTPException(
                status_code=500,
                detail=f"Error parsing JSON response: {str(e)}"
            )

    except HTTPStatusError as e:
        if e.response.status_code == 429:
            raise HTTPException(
                status_code=429,
                detail="Limite de requêtes atteinte. Veuillez réessayer dans quelques minutes."
            )
        raise HTTPException(
            status_code=500,
            detail="Une erreur est survenue lors de l'analyse"
        )
    except Exception as e:
        logger.error(f"Erreur lors de l'analyse: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Une erreur inattendue est survenue"
        ) 