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
brands.py : contient la classe Brands
categories.py : contient la classe Categorie
conf.json : contient les configurations relatives au programme
data_treatment.py : contient les méthodes pour nettoyer les données et les préparer à l'insertion dans la base de données
ingredients.py : Contient la classe Ingredients
language.json : contient les textes des menus en anglais et en français
link_api : Permet de faire des requêtes sur l'API d'openfoodfacts (Classe : Link_API)
link_db.py : Méthodes de connexion à la base de données mysql ( Classe : Link_DB)
menu.py : Classe Menu permettant de gérer l'affichage des menus du programme
nutrition_grade.py : contient la classe Nutrition_grade
products.py : contient la classe Products
read_txt.py : contient les méthodes pour récupérer des informations depuis un fichier texte
requirements.txt : indique les bibliothèques python à installer
run.py : permet de lancer le programme

Schema : dossier contenant les schémas relatifs à la conception du programme
	- MLD-v1 : Première version du MLD de la base de données
SQL: dossier contenant les scripts SQL pour intéragir avec la base de données MySQL openfoodfacts
	- create_tables.sql : scripts de création des tables
	- delete_tables.sql : script de suppression des tables

-------------------------
Utilisation du programme
-------------------------
Installer les bibliothèques python indiquées dans requirements.txt
Renommer conf_example.json en conf.json et changer les informations de connexion à la BDD.