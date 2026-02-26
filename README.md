# Projet_5
Maintenez et documentez un système de stockage des données sécurisé et performant

## Contexte :

Sous la supervision de mon chef de projet Boris, je me suis penché sur la migration de données depuis un dataset CSV vers une instance MongoDB sous Docker.
Pour ce faire, il faut écrire un script d’intégration de données et expliquer le processus dans un README.md qui sera sur un dépôt GitHub.
Les différentes étapes vont être :

- Schéma de l’architecture souhaitée
- Création du dépôt GitHub et clonage de celui-ci en local
- Construction du docker-compose.yml et du Dockerfile
- Ecriture du script d’intégration
- Connexion de la base de données sur Compass
- Test du processus en suivant la documentation du README

## Lancement du script d'intégration des données :

Tout d'abord, il faut lancer le conteneur, si jamais c'est la première fois, alors il faut lancer cette commande :

> docker-compose up -d --build

Si ce n'est pas la première fois, alors il faut lancer cette commande :

> docker-compose up -d

Ensuite, il faut rentrer dans le conteneur, pour ce faire, il faut rentrer cette commande :

> docker exec -it "nom du conteneur" bash

Une fois rentrer dedans, il faut se rendre dans le dossier script :

> cd /scripts

Et lancer le script :

> python "nom du script"

## Fonctionnement du script d'intégration des données :

Dans un premier temps on vient récupérer les informations de connexion à la base de données :
- > mongo = MongoClient('mongodb://root:a1B2c3D4e5@db:27017/')
- > db = mongo['local']
- > collection = db['data']

On indique que l'on souhaite accéder à la base de données qui se nomme **local** et la collection qui se nomme **data**.

Ensuite, à l'aide du package *pandas*, on vient récupérer le fichier csv, le lire, transformer les informations en un dictionnaire python :

> df = pd.read_csv('dataset/healthcare_dataset.csv')

> data = df.to_dict(orient='records')

Et enfin, intégrer ces informations à la base avec :

> collection.insert_many(data)