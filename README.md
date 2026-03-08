# 🚖 Uber Sentiment AI : Analyse Sémantique & Système RAG

> *Transformer 12 000 avis d'utilisateurs en décisions stratégiques grâce à l'IA Générative et au Machine Learning.*

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![OpenAI](https://img.shields.io/badge/AI-OpenAI%20API-green)
![LangChain](https://img.shields.io/badge/Framework-LangChain-orange)
![Streamlit](https://img.shields.io/badge/App-Streamlit-red)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-yellow)

## 📸 Aperçu de l'Application (Interface Streamlit)
Interface conversationnelle permettant aux équipes d'interroger la base de données vectorielle contenant les 12 000 avis.
![Interface Streamlit Uber AI](reports/Capture-du-chatboot.png)

---

## 🎯 Objectif Métier (Business Case)
Face au volume massif de retours clients, l'analyse manuelle est impossible. L'objectif de ce projet est de doter les équipes produit et service client d'Uber d'un pipeline automatisé capable de :
1. **Classifier automatiquement les motifs d'insatisfaction** (Data Wrangling & Prompt Engineering).
2. **Évaluer l'urgence (Score de Gravité)** de chaque plainte pour prioriser les actions.
3. **Interroger la base de connaissances en langage naturel** pour obtenir des insights ciblés (Système RAG).

## 🛠️ Stack Technique & Compétences
Ce projet combine les méthodologies de la certification **Google Advanced Data Analytics** (rigueur statistique) et **IBM Generative AI Engineer** (implémentation de LLM).

* **Data Science (Google) :** Pandas, Matplotlib, Seaborn (Visualisation à double axe).
* **Intelligence Artificielle (IBM) :** OpenAI API (GPT-3.5-Turbo), Prompt Engineering (Format JSON strict).
* **Ingénierie RAG :** LangChain, Base de données vectorielle ChromaDB, Embeddings textuels, Streamlit.
* **Machine Learning :** Scikit-Learn (TF-IDF, Régression Logistique).

---

## 📊 Méthodologie : Framework PACE

Le projet est structuré selon le framework **PACE** (Plan, Analyze, Construct, Execute) :

### 1. Plan & Analyze (EDA)
Nettoyage de 12 000 avis, gestion des doublons, et analyse de la distribution des notes (polarisation en 'U' très marquée). Confirmation de la corrélation entre la note (1 étoile) et la longueur du texte.

### 2. Construct & Execute (Pipeline RAG & IA Générative)
* **Extraction Sémantique :** Traitement de masse via API pour extraire la Catégorie, le Sentiment et un Score d'Urgence (1-10) sur un échantillon critique.
* **Cerveau Vectoriel :** Création d'un système RAG (Retrieval-Augmented Generation) avec LangChain et ChromaDB pour "discuter" avec les avis.

### 3. Bonus : Modélisation Prédictive (NLP)
Entraînement d'un modèle de Régression Logistique pénalisé (`class_weight='balanced'`) pour prédire la note d'un utilisateur uniquement à partir de son texte.
![Matrice de Confusion](assets/confusion_matrix.png)
*Insight : Le modèle excelle dans la détection des extrêmes (1 et 5 étoiles) grâce à une vectorisation TF-IDF performante.*

---

## 🚀 Résultats Stratégiques (AI-Driven Insights)

Le pipeline d'IA a révélé une matrice de décision cruciale pour la direction (Fréquence vs Urgence) :

![Analyse Réelle Fréquence vs Urgence](assets/real_analysis.png)

1. **🚨 Le Paradoxe de la Sécurité (Urgence Absolue) :** Bien qu'elle ne représente qu'environ 10% des plaintes, la thématique **SECURITE** génère le score de risque le plus élevé (>90/100). C'est un signal faible mais critique nécessitant une action immédiate.
2. **💸 L'Attrition Quotidienne (Bruit de fond) :** Le **PRIX** (tarification obscure, frais) est le problème le plus fréquent (>40% des plaintes), suivi de près par la **TECHNIQUE** (bugs). Ce sont les irritants majeurs qui nuisent à la rétention.

---

## ⚙️ Installation & Utilisation

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/VOTRE_PSEUDO/uber-sentiment-ai.git](https://github.com/VOTRE_PSEUDO/uber-sentiment-ai.git)
   cd uber-sentiment-ai
