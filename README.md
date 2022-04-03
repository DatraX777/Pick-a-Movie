# MongoDB

Pour build le prjet il faut d'abbord build les images.

Pour cela aller dans le dossier build du dossier pymongo et executer la commande suivante:
        docker build -t crud:latest

Aller ensuite dans le dossier build du dossier NetflixLike et executer la commande suivante:
        docker build -t vueweb:latest

Finalement executer docker-compose up -d dans le dossier global pour lancer la composition des container