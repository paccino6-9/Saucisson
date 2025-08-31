# Cave à Saucisson App

Ce projet est une application pour piloter une cave à saucisson à l'aide d'un Raspberry Pi. Il utilise un capteur BME280 pour surveiller les conditions environnementales et des relais pour contrôler un humidificateur, un ventilateur et un appareil auxiliaire.

## Structure du Projet

```
cave-saucisson-app
├── backend
│   ├── app.py                # Point d'entrée de l'application backend
│   ├── relay_control.py      # Gestion des relais
│   ├── bme280_sensor.py      # Interaction avec le capteur BME280
│   └── config.py             # Configurations de l'application
├── frontend
│   ├── static
│   │   └── style.css         # Styles CSS pour le frontend
│   └── templates
│       └── index.html        # Modèle HTML principal
├── requirements.txt          # Dépendances Python nécessaires
├── README.md                 # Documentation du projet
└── .env                      # Variables d'environnement
```

## Installation

1. Clonez le dépôt :
   ```
   git clone <URL_DU_DEPOT>
   cd cave-saucisson-app
   ```

2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

3. Configurez les variables d'environnement dans le fichier `.env`.

## Utilisation

1. Démarrez l'application backend :
   ```
   python backend/app.py
   ```

2. Accédez à l'interface utilisateur via votre navigateur à l'adresse `http://localhost:5000`.

## Fonctionnalités

- Surveillance de la température, de l'humidité et de la pression grâce au capteur BME280.
- Contrôle des relais pour gérer l'humidificateur, le ventilateur et un appareil auxiliaire.
- Interface utilisateur simple pour visualiser les données et contrôler les appareils.

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une demande de tirage pour toute amélioration ou correction.