# coding : utf-8

#Own classes and libraries
from menu import Menu

#Project classes and libraries
from link_db import Link_DB

language_menu = Menu("language_menu")
language_menu.display()

Link_DB.connexion_with_conf_file("conf.json")
