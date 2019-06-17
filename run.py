# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Project classes and libraries
from Classes.link_api import Link_API
from Classes.link_db import Link_DB
from Classes.menu import Menu
from Classes.products import Products

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
    main_menu_input = 0

    #While the user chose the wrong main menu, we display it again
    while int(main_menu_input) < 1 or int(main_menu_input) > main_menu.num_options:
        main_menu.display()
        main_menu_input = input("=> ")
        os.system("clear")

    #If the user choses to insert datas in database
    if main_menu_input == "1":
        print("Insert data")
        link = Link_API()
        urls = ["pizzas", "sandwich"]
        answer = link.request_from_list(urls)
        print(answer)
        

    #If user chose to exit the program
    if main_menu.options[main_menu_input] == "Exit" or main_menu.options[main_menu_input] == "Quitter":
        exit_program = True



#Link_DB.connexion_with_conf_file("conf.json")
