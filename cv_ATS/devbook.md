# Analyseur de CV avec IA
## 🎯 Vue d'ensemble

Application web permettant d'analyser automatiquement des CV via l'intelligence artificielle, en simulant le comportement des ATS (Applicant Tracking Systems).

## 💡 Fonctionnalités principales

- Upload de CV au format PDF
- Analyse complète du CV :
  - Lisibilité et structure 
  - Détection des mots-clés importants
  - Optimisation SEO pour les recruteurs
  - Compatibilité avec une offre d'emploi (optionnel)
- Suggestions d'amélioration personnalisées
- Export du CV optimisé

## 🛠 Architecture technique

| Composant | Technologie |
|-----------|-------------|
| API Backend | FastAPI |
| Modèle IA | Groq API (Mixtral) |
| Parser PDF | PyMuPDF |
| Frontend | Vue.js 3 + Vite |
| Infrastructure | Docker + Traefik |

## 🔄 Processus d'analyse

1. **Réception du CV**
   - Upload du fichier PDF
   - Saisie optionnelle d'une offre d'emploi

2. **Extraction et validation**
   - Conversion PDF vers texte
   - Vérification du format et de la lisibilité
   - Détection des éléments problématiques

3. **Analyse IA**
   - Génération du prompt expert ATS
   - Envoi du CV et de l'offre (optionnelle) à l'API Groq
   - Analyse détaillée :
     - Format et structure du document
     - Mots-clés pertinents (top 40)
     - Lisibilité des éléments
     - Score global sur 20 points
   - Suggestions d'optimisation

4. **Présentation des résultats**
   - Tableau de scores détaillés (/5 par critère)
   - Liste des mots-clés manquants
   - Alertes sur les éléments problématiques
   - Version optimisée du CV

## 💻 Frontend

### Technologies utilisées
- Vue.js 3 avec Composition API
- TailwindCSS pour le styling

### Structure du projet

### Options d'import du CV

#### ✅ Option 1 - Copier-coller
- Champ texte simple pour coller le contenu du CV
- Traitement direct sans parsing
- Solution rapide et légère
- Idéal pour le MVP et les tests

#### 🆙 Option 2 - Upload PDF
- Formulaire avec input type="file"
- Restriction aux fichiers .pdf
- Parsing côté serveur avec PyMuPDF
- Support de la mise en forme et structure

### Interface utilisateur
- Design épuré et intuitif
- Choix entre les deux modes d'import
- Champ optionnel pour l'offre d'emploi
- Bouton "Analyser" déclenchant la requête Groq
- Affichage des résultats structuré et clair

## 📡 API Backend
### Structure de l'API

#### Endpoints

1. `/api/analyze-cv`
   - Méthode : POST
   - Corps de la requête :
     ```typescript
     {
       cvContent: string;
       jobOffer?: string; // Optionnel
     }
     ```
   - Réponse :
     ```typescript
     {
       hasTitle: boolean;        // Présence d'un titre clair
       titleFeedback: string;    // Retour sur le titre
       hasGoodStructure: boolean;// Structure correcte
       structureFeedback: string;// Retour sur la structure
       missingKeywords: string[];// Mots-clés manquants du top 40
       alerts: string[];         // Alertes (format, lisibilité...)
       optimizedVersion: string; // Version améliorée du CV
     }
     ```

#### Traitement

1. Nettoyage et préparation
   - Suppression des caractères spéciaux
   - Normalisation du texte
   - Extraction de la structure

2. Analyse via Groq
   - Construction du prompt expert
   - Appel API avec streaming
   - Parsing de la réponse

3. Formatage des résultats
   - Conversion en objet TypeScript
   - Validation des données
   - Enrichissement des retours


### Analyse simple