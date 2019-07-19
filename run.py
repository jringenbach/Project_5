# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Project classes and libraries
from Classes.categorie import Categorie
from Classes.linkapi import LinkAPI
from Classes.linkdb import LinkDB
from Classes.menu import Menu
from Classes.product import Product

import data_treatment
import read_txt

#Python classes and libraries
import os

#--------------------------------------------------------------------
#                           MAIN PROGRAM
#--------------------------------------------------------------------

exit_program = False

#Instanciation of the language choice menu
language_menu = Menu("language_menu", None)
language = str()

#While the user doesn't chose "fr" or "en", we keep asking him the language
while(language != "fr" and language != "en"):
    language_menu.display()
    language = input(" => ")
    os.system("clear")

#We change the language in the conf.json if it is necessary
language_menu.change_language(language)

#While the user hasn't chosen to exit the program
while not exit_program:
    #We instanciate the main menu
    main_menu = Menu("main_menu", None)
    main_menu_input = main_menu.input()

    #If the user choses the database menu
    if main_menu_input == "1":

        database_menu = Menu("database_menu", None)
        database_menu_input = database_menu.input()

        #If user choses to insert data in database from openfoodfacts
        if database_menu_input == "1":
            #List of Categories Object
            list_categories = list()
            list_categories_txt = read_txt.get_list_from_txt_file("categories.txt")
            
            #We get every products for each categorie
            for categorie_str in list_categories_txt:
                categorie = Categorie(categorie_str)
                categorie.get_products_by_categorie() #Request API for this categorie and get the products
                list_categories.append(categorie)

            #We create a dict with all datas and we clean the datas
            openfoodfacts_dict = data_treatment.get_list_of_all_objects(list_categories)
            openfoodfacts_dict = data_treatment.clean_datas(openfoodfacts_dict)

            #We create the tables in the database if they don't exist
            link_to_database = LinkDB()

            #We try to execute the "creation tables" script
            try:
                link_to_database.execute_sql_script_from_file("SQL/create_tables.sql")
            except:
                print("Tables already exist.")
            finally:
                link_to_database.link_classes_to_orm(openfoodfacts_dict)
                link_to_database.insert_datas_to_database(openfoodfacts_dict)


        #Exit the program from database menu
        elif database_menu_input == "4":
            exit_program = True


    #If the user chooses "My nutritional Program" in the main menu
    elif main_menu_input == "2":
        
        link_to_database = LinkDB()
        dict_of_categorie = link_to_database.get_dict_of_categories_from_database()
        categorie_menu = Menu(None, dict_of_categorie)
        categorie_menu.display()


        

    #If user chose to exit the program
    if main_menu.options[main_menu_input] == "Exit" or main_menu.options[main_menu_input] == "Quitter":
        exit_program = True


