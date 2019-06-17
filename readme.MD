---- OpenFoodFacts ----



-------------------------
Informations générales
-------------------------
Pip 19.1
Python 3.7


-------------------------
A faire sur le projet
-------------------------
Création de la base de données MySQL
Création de l'interface du terminal de commande
Insérer des données dans la base de données
Lire les données depuis la base de données
Permettre à l'utilisateur de créer des favoris

-------------------------
Que doit faire le programme?
-------------------------
Si la base de données relative au projet n'a pas été créée, alors il est possible que le script créé la base de données
de lui-même. Ensuite, il doit permettre de pouvoir récupérer les informations d'openfoodfacts et de les insérer dans la base
de données. 
L'utilisateur doit pouvoir être capable de lire les informations enregistrées précédemment dans le programme pour
retrouver ses aliments favoris.


-------------------------
Fichiers
-------------------------
language.json : contient les textes des menus en anglais et en français
link_db.py : Méthodes de connexion à la base de données mysql ( Classe : Link_DB)
menu.py : Classe Menu permettant de gérer l'affichage des menus du programme
requirements.txt : indique les bibliothèques python à installer
run.py : permet de lancer le programme

-------------------------
Utilisation du programme
-------------------------
Installer les bibliothèques python indiquées dans requirements.txt
Renommer conf_example.json en conf.json et changer les informations de connexion.