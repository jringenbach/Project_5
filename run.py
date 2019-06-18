# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Project classes and libraries
from Classes.categories import Categorie
from Classes.link_api import Link_API
from Classes.link_db import Link_DB
from Classes.menu import Menu
from Classes.products import Products

import data_treatment
import read_txt

#Python classes and libraries
import os

#--------------------------------------------------------------------
#                           MAIN PROGRAM
#--------------------------------------------------------------------

exit_program = False

#Instanciation of the language choice menu
language_menu = Menu("language_menu")
language = str()

#While the user doesn't chose fr or en, we keep asking him the language
while(language != "fr" and language != "en"):
    language_menu.display()
    language = input(" => ")
    os.system("clear")

#We change the language in the conf.json if it is necessary
language_menu.change_language(language)

#While the user hasn't chosen to exit the program
while not exit_program:
    #We instanciate the main menu
    main_menu = Menu("main_menu")
    main_menu_input = main_menu.input()

    #If the user choses the database menu
    if main_menu_input == "1":

        database_menu = Menu("database_menu")
        database_menu_input = database_menu.input()

        #If user choses to insert data in database from openfoodfacts
        if database_menu_input == "1":
            #List of Categories Object
            list_categories = list()
            list_categories_txt = read_txt.get_list_from_txt_file("categories.txt")
            
            #We get every products for each categorie
            for item in list_categories_txt:
                categorie = Categorie(item)
                categorie.get_products_by_categorie()
                list_categories.append(categorie)

            openfoodfacts_dict = data_treatment.get_list_of_all_objects(list_categories)
            data_treatment.find_all_duplicates(openfoodfacts_dict)

        #Exit the program from database menu
        elif database_menu_input == "4":
            exit_program = True
        

    #If user chose to exit the program
    if main_menu.options[main_menu_input] == "Exit" or main_menu.options[main_menu_input] == "Quitter":
        exit_program = True


