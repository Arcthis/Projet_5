# Projet_5
Maintenez et documentez un système de stockage des données sécurisé et performant

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