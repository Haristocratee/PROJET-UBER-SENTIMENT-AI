# 🚖 Uber Sentiment AI : Analyse Sémantique & Système RAG

> *Transformer 12 000 avis d'utilisateurs en décisions stratégiques grâce à l'IA Générative et à l'analyse de données.*

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![OpenAI](https://img.shields.io/badge/AI-OpenAI%20API-green)
![LangChain](https://img.shields.io/badge/Framework-LangChain-orange)
![Pandas](https://img.shields.io/badge/Data-Pandas%20%7C%20Seaborn-lightgrey)

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
* **Ingénierie RAG :** LangChain, Base de données vectorielle ChromaDB, Embeddings textuels.

---

## 📊 Méthodologie : Framework PACE

Le projet est structuré selon le framework **PACE** (Plan, Analyze, Construct, Execute) :

* **Notebook 1 : Plan & Analyze (`1_Uber_Analysis_PACE.ipynb`)** * Nettoyage de 12 000 avis (doublons, valeurs manquantes).
  * Analyse de la distribution des notes (polarisation en 'U' très marquée).
  * Corrélation entre la note (1 étoile) et la longueur du texte (les insatisfaits écrivent plus).
  * *Construct :* Traitement de masse via API pour extraire la Catégorie, le Sentiment et un Score d'Urgence (1-10) sur un échantillon critique.

* **Notebook 2 : Construct & Execute (`2_Uber_RAG_System.ipynb`)**
  * *Construct :* Création d'un système RAG (Retrieval-Augmented Generation) pour "discuter" avec les avis.
  * *Execute :* Synthèse exécutive et dataviz croisant la Fréquence des problèmes avec leur Urgence.

---

## 🚀 Résultats Stratégiques (AI-Driven Insights)

Le pipeline d'IA a révélé une matrice de décision cruciale pour la direction (Fréquence vs Urgence) :

1. **🚨 Le Paradoxe de la Sécurité (Urgence Absolue) :** Bien qu'elle ne représente qu'environ 10% des plaintes, la thématique **SECURITE** génère le score de risque le plus élevé (>90/100). C'est un signal faible mais critique nécessitant une action immédiate.
2. **💸 L'Attrition Quotidienne (Bruit de fond) :** Le **PRIX** (tarification obscure, frais) est le problème le plus fréquent (~41% des plaintes), suivi de près par la **TECHNIQUE** (bugs). Ce sont les irritants majeurs qui nuisent à la rétention.
3. **👤 Le Comportement (Risque intermédiaire) :** Les problèmes liés aux chauffeurs nécessitent des alertes automatisées pour prévenir les dérives vers des cas de sécurité.

---

## ⚙️ Installation & Utilisation

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/VOTRE_PSEUDO/uber-sentiment-ai.git](https://github.com/haristocratee/uber-sentiment-ai.git)
   cd uber-sentiment-ai