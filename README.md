# Projet FastAPI - tp-Achat-FastApi

Ce projet est une API REST développée avec FastAPI, qui inclut une structure modulaire, des dépendances essentielles, et les bonnes pratiques pour une gestion efficace du dépôt.

## Table des Matières
1. [Pré-requis](#pré-requis)
2. [Installation et Configuration](#installation-et-configuration)
3. [Structure du Projet](#structure-du-projet)
4. [Lancer l'application](#lancer-lapplication)
5. [Gestion des Dépendances](#gestion-des-dépendances)
6. [Bonnes Pratiques pour le Push](#bonnes-pratiques-pour-le-push)

---

### 1. Pré-requis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :
- **Python 3.10+**
- **Git** (pour le contrôle de version)
- **Virtualenv** (ou utilisez `python -m venv` pour les environnements virtuels)

---

### 2. Installation et Configuration

Suivez les étapes ci-dessous pour configurer le projet FastAPI.

1. **Cloner le dépôt** :
   ```bash
   git clone <URL_DU_DEPOT>
   cd tpAchatFastAPI

Créer un environnement virtuel :
   ```bash
   python -m venv env
   ```

Activer l'environnement virtuel :
   ```bash
   .\env\Scripts\activate
   ```

### 3. **structure-du-projet** : 

tpAchatFastAPI/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/ 
│   │   └── prediction_routes.py # Nouveau : Route de prédiction
│   ├── models/
│   ├── schemas/
│   │   └── prediction.py # Nouveau : Route de prédiction
│   ├── services/
│   │   └── prediction_service.py # Nouveau : Route de prédiction
│   └── services/
├── ml/                         # Nouveau : Dossier pour les fichiers ML
│   ├── __init__.py
│   ├── train.py                # Script pour entraîner les modèles
│   ├── predict.py              # Script pour effectuer des prédictions
│   ├── preprocess.py           # Script de pré-traitement des données
│   ├── model/                  # Modèles sauvegardés
│   └── data/                   # Données pour l'entraînement et les tests
│       
├── tests/                      # Nouveau : Tests unitaires et d'intégration
│   ├── __init__.py
│   ├── test_api.py             # Tests pour l’API
│   ├── test_ml.py              # Tests pour les fonctions ML
│   └── ...
├── .github/
│   └── workflows/
│       └──  ci_mlops_pipeline.yml  # Nouveau : Pipeline GitHub Actions
├── requirements.txt
└── README.md


### 4. **lancer-lapplication** :

  ```bash
  uvicorn app.main:app --reload
  ```

### 5. **gestion-des-dépendances** :

Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   
   pip freeze > requirements.txt
   
   pip list

   ```


### 5. **bonnes-pratiques-pour-le-push** :


