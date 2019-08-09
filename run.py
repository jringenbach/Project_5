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

from ORM.registeredproductdb import RegisteredProductDB

import data_treatment
import read_txt

#Python classes and libraries
import os

#--------------------------------------------------------------------
#                           MAIN PROGRAM
#--------------------------------------------------------------------

exit_program = False
language = "fr"


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


        #If the user wants to delete the table from the database
        elif database_menu_input == "2":
            link_to_database = LinkDB()

            #We try to execute the "deletion tables" script
            try:
                link_to_database.execute_sql_script_from_file("SQL/delete_tables.sql")
            except:
                print("Couldn't delete table from database")


        #Exit the program from database menu
        elif database_menu_input == "4":
            exit_program = True


    #If the user chooses "My nutritional Program" in the main menu
    elif main_menu_input == "2":

        nutritional_menu = Menu("nutritional_program_menu")
        nutritional_menu_input = nutritional_menu.input()
        
        link_to_database = LinkDB()


        #If the user want to find a substition product
        if nutritional_menu_input == "1":

            #We get the list of the categories from the database and we display it as a menu
            dict_of_categorie = link_to_database.get_dict_of_categories_from_database()
            categorie_menu = Menu(None, dict_of_categorie)
            categorie_chosen = categorie_menu.input()

            #We get the dict of product from the categorie chosen by the user
            dict_of_products = link_to_database.get_dict_of_products_from_database(dict_of_categorie[categorie_chosen].id_categorie)
            product_menu = Menu(None, dict_of_products)
            num_product_chosen = product_menu.input()
            product_chosen = dict_of_products[num_product_chosen]

            #We get the list of product with better nutrition grade and display them
            list_product_with_better_nutrition_grade = link_to_database.get_list_of_product_with_better_nutrition_grade(dict_of_products, dict_of_products[num_product_chosen])
            product_substitute = data_treatment.print_list_of_products(list_product_with_better_nutrition_grade)

            register_product_menu = Menu("register_product_menu")
            register_product_input = register_product_menu.input()

            #If the user wants to register the product of substitution in the database
            if register_product_input == "1":

                #We insert the product chosen and its substitution product into the database
                if product_substitute is not None:
                    registeredproductdb_to_insert = RegisteredProductDB(product_chosen.barcode, product_substitute.barcode)
                    registeredproductdb_to_insert.insert_to_database(link_to_database.db)


        #If the user wants to see the product he/she has already looked for substitute
        elif nutritional_menu_input == "2":
            print("Retrouver mes aliments substitués")
            dict_product_and_substitute = link_to_database.get_list_of_product_and_substitute_from_database()
            data_treatment.print_product_and_substitute(dict_product_and_substitute)

        

    #If user chose to exit the program
    if main_menu.options[main_menu_input] == "Exit" or main_menu.options[main_menu_input] == "Quitter":
        exit_program = True


