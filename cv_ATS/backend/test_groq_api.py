from openai import OpenAI

# Initialisation du client avec la clé Groq
client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

# Exemple de prompt simple
prompt = """
Tu possèdes la double expertise en ATS (Applicant Tracking Systems ou systèmes de suivi des candidatures) à succès sur le marché mais aussi en recrutement.  Plus précisément, tu as une parfaite connaissance du fonctionnement des ATS présents sur le marché, de leurs techniques de traitement du langage naturel (NLP) et d'analyse sémantique pour identifier et structurer les données clés (nom, coordonnées, expérience professionnelle, compétences, formations, etc.). Tu maîtrises également parfaitement les techniques SEO mais aussi les intitulés de postes ainsi que les mots-clefs les plus utilisés pour chacun d'entre eux dans la rédaction des offres d'emploi.  

Tu as deux fonctions :  

1)    Si on te joint seulement un CV sans offre d'emploi = Evaluation du CV seul. Evalue l'efficacité du CV pour passer les ATS qui te sera proposé en dressant un tableau dans lequel tu attribueras une note sur 5 à chaque item et en proposant un point d'amélioration si besoin. Ajuste la somme des points sur 20. Les items d'évaluation seront : 
o    Présence d'un titre clair et lisible 
o    Le format du CV : PDF, Word. Alerte si c'est un format image (jpeg, png…) ou un PDF plat. 
o    La structure du CV : présence de titres de section clairs. 
o    Le recensement des 40 mots clefs les plus utilisés pour cet intitulé de poste dans les offres d'emploi (liste tous les mots clefs manquants sur les 40 qui devraient être présents = génère si possible un fichier avec tous les mots-clefs à intégrer à mon CV). 
o    Si tu détectes des images autres que la photo de profil ou des abréviations, alerte sur l'absence de lisibilité ou le risque de manque de lisibilité de ces informations. 
o    Si tu détectes d'autres éléments illisibles : tableau, zone de texte = alerte. 
o    Propose une version du CV optimisé selon tous les points d'amélioration que tu auras relevé. 

2)    Si on te joint un CV et une offre d'emploi = Evaluation du CV en fonction d'une offre d'emploi : Evalue l'efficacité du CV pour passer les ATS qui te sera proposé en fonction de l'offre d'emploi qui te sera jointe. Tu dresseras un tableau dans lequel tu attribueras une note sur 5 à chaque item et en proposant un point d'amélioration si besoin. Ajuste la somme des points sur 20. Utilise les mêmes items que ceux cités précédemment.
Voici un CV fictif :

Jean Dupont  
Développeur Python  
Expérience : 3 ans chez Airbus, 2 ans chez Capgemini  
Compétences : Python, Docker, Git, FastAPI  
Formation : Master Informatique, Université Toulouse III

Évalue ce CV pour un poste de Développeur Back-end, selon les critères d'un ATS.
"""


# Appel au modèle Llama 3.3 via Groq
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    stream=True
)

# Remplacer la partie qui gère la réponse
try:
    # Si vous voulez une réponse en streaming
    for chunk in response:
        if hasattr(chunk.choices[0].delta, "content"):
            print(chunk.choices[0].delta.content, end="")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

# OU si vous préférez une réponse complète sans streaming
try:
    # Récupérer le dernier chunk du stream
    completion = ""
    for chunk in response:
        if hasattr(chunk.choices[0].delta, "content"):
            completion += chunk.choices[0].delta.content
    print(completion)
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
