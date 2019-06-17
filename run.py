# coding : utf-8

#Own classes and libraries
from menu import Menu

#Project classes and libraries
from link_db import Link_DB

#Instanciation of the language choice menu
language_menu = Menu("language_menu")
language = str()

#While the user doesn't chose fr or en, we keep asking him the language
while(language != "fr" and language != "en"):
    language_menu.display()
    language = input(" => ")

#We change the language in the conf.json if it is necessary
language_menu.change_language(language)

#We instanciate the main menu
main_menu = Menu("main_menu")
main_menu.display()

#Link_DB.connexion_with_conf_file("conf.json")
