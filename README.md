# Urban Transit Forecast 🚇

Projet de Data Analysis & Prédiction sur l'affluence des transports urbains.

## 🎯 Contexte et But du projet

L’affluence dans les transports urbains varie fortement selon plusieurs facteurs :

les horaires (heures de pointe, week-end, vacances),

les conditions météorologiques (pluie, chaleur, vent),

le calendrier (jours fériés, événements particuliers).

L’objectif de ce projet est de collecter, analyser et prédire ces variations de fréquentation afin de mieux comprendre et anticiper l’usage des transports.

Ce projet illustre une démarche complète de Data Analysis & Data Science appliquée à un cas concret de mobilité urbaine.

## 🔍 Objectifs

Collecter des données publiques (fréquentation RATP + météo Open-Meteo).

Nettoyer et croiser les données pour les rendre exploitables.

Analyser les tendances (pics horaires, influence de la météo, impact des jours fériés).

Construire un modèle simple de prévision (ex : Prophet).

Développer un dashboard interactif (Power BI ou Streamlit).

## Structure du projet

urban-transit-forecast/
│
├── data/                # Données du projet
│   ├── raw/             # Données brutes collectées
│   └── processed/       # Données nettoyées / transformées
│
├── notebooks/           # Analyses exploratoires et modèles
│
├── src/                 # Code source ETL
│   └── etl/             # Scripts d’ingestion et nettoyage
│
├── README.md            # Documentation du projet
└── requirements.txt     # Dépendances Python


## Roadmap
- [x] Collecte des données
- [ ] Nettoyage et préparation
- [ ] Analyse exploratoire (EDA)
- [ ] Modélisation
- [ ] Dashboard interactif
- [ ] Documentation et mise en ligne

## ⚙️ Prérequis

- Python 3.10+

- Créer et activer un environnement virtuel :
python -m venv .venv
.venv\Scripts\activate  # Windows

- Installer les dépendances :
python -m pip install -r requirements.txt



## Comandes utiles :

- Afficher ce qui a dans le dossier : ls
- Acceder a un dossier: cd 
- Recuperer le chemin courant exemple : pwd       
Ex : C:\Users\Raissa\Desktop\Projet_perso\urban-transit-forecast\src\etl
- Activer l'environnement : .venv\Scripts\activate
- Installer les package : python -m pip install nom_du_package 
- verifier si Package installé :python -c "import requests, pandas; print('✅ Tout est OK !')" :
- vider le terminal : cls
- Quelle branche je suis : git branch
- Créer une nouvelle branche : git checkout -b feature/ingest-meteo
git push -u origin feature/ingest-meteo


lien vers data RATP 2013 :https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre/information/
