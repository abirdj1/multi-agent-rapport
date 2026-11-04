#  Strategic Report Agent - Système Multi-Agents IA

> **Générez des rapports stratégiques de niveau McKinsey en 3 minutes** grâce à 4 agents IA collaboratifs.

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Latest-FF6B6B?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🎯 Vue d'ensemble

**Strategic Report Agent** est un système multi-agents IA qui automatise la création de rapports stratégiques professionnels. Quatre agents spécialisés collaborent de manière séquentielle pour produire des analyses complètes avec sources vérifiables, opportunités chiffrées et recommandations actionnables.

**️ Temps de génération** : 2-3 minutes  
**💰 Coût par rapport** : ~0€ (OpenRouter gratuit)  
**📊 Qualité** : Niveau cabinet de conseil

---

## 🎬 Démo Vidéo

> 📹 **Voir le système en action** : [Lien vers votre vidéo de démo]

*(Remplacez ce lien par votre vidéo YouTube non-listée ou GIF après avoir créé la démo)*

---

## ✨ Fonctionnalités

###  Intelligence Artificielle
- **4 agents spécialisés** avec prompts de niveau expert
- **Recherche internet en temps réel** via DuckDuckGo (8+ sources)
- **Croisement de sources** pour éliminer les hallucinations
- **Retry automatique** (3 tentatives) en cas d'erreur réseau

### 📊 Qualité Professionnelle
- **Structure en 9 sections** (Résumé, Contexte, Analyse, Opportunités, Risques, Recommandations, Sources)
- **Ton cabinet de conseil** (factuel, orienté décision)
- **Sources traçables** avec liens cliquables
- **Précautions méthodologiques** pour les données non-auditées

###  Interface & Export
- **Interface web Streamlit** intuitive
- **Export double format** : Markdown + PDF stylisé
- **Téléchargement en 1 clic**
- **Sauvegarde automatique** dans `outputs/`

---

## 🏗️ Architecture
─────────────────────────────────────────────────────┐
│ INTERFACE STREAMLIT (app.py) │
└──────────────────────┬──────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────
│ MOTEUR CREWAI (main.py) │
└──┬──────────┬──────────┬──────────┬─────────────────┘
│ │ │ │
▼ ▼ ▼ ▼
──────┐ ┌────────┐ ┌─────────┐ ┌────────┐
│Re- │▶│ Ana- │▶│ Stra- │▶│ Writer │
│sear- │ │ lyst │ │ tegist │ │ │
│cher │ │ │ │ │ │ │
└──┬───┘ └────────┘ ─────────┘ └───┬────┘
│ │
▼ ▼
┌──────────┐ ┌──────────────┐
│DuckDuckGo│ │ .md + .pdf │
└──────────┘ ──────────────┘



| Agent | Rôle | Output |
|-------|------|--------|
| 🔍 **Researcher** | Chercheur Expert | 5-8 sources fiables avec données chiffrées |
|  **Analyst** | Analyste Senior | 3-5 tendances majeures avec preuves |
|  **Strategist** | Directeur Stratégie | Opportunités + Risques + Roadmap |
| ✍️ **Writer** | Rédacteur Expert | Rapport final structuré (800+ mots) |

---

##  Installation Rapide

### Prérequis
- Python 3.13+
- Clé API OpenRouter gratuite : [openrouter.ai/keys](https://openrouter.ai/keys)

### 4 étapes

```bash
# 1. Cloner le repository
git clone https://github.com/abirdj1/multi-agent-rapport.git
cd multi-agent-rapport

# 2. Installer les dépendances
pip install crewai crewai-tools duckduckgo-search python-dotenv litellm streamlit markdown xhtml2pdf

# 3. Configurer la clé API
# Créer un fichier .env avec : OPENROUTER_API_KEY=sk-or-v1-...

# 4. Lancer l'application
streamlit run app.py