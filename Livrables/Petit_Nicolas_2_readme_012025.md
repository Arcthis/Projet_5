# Projet_5
Maintenez et documentez un système de stockage des données sécurisé et performant

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