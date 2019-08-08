# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#My own libraries
from Classes.categorie import Categorie
from Classes.product import Product
from ORM.categoriedb import CategorieDB

#Python libraries
import json
import os


class Menu:
    """Handles menus of the program and all their methods

    language : language of the menu (str)
    options : options of the menu that will be displayed (str or dict)
    num_options : number of options in the menu (int)"""



    def __init__(self, menu_name=None, options_dict=None):
        """Initialization of a menu"""
        self.options = dict()
        self.num_options = int()


        if menu_name is None:
            self.create_menu_from_dict(options_dict)

        else:
            self.language = self.search_language_used()
            self.options = self.get_options_from_json(menu_name)
            if type(self.options) is str:
                self.num_options = 1
            else:
                self.num_options = len(self.options)
            print(self.num_options)



#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------


    def calculate_max_length_options(self):
        """Look into the options the one with the longest length and return its length
        
        max_length : size of the longest string in the dict of menus (int)"""

        max_length = -1

        #We go through options and depending on their type, we set len_option
        for key, option in self.options.items():
            if type(option) is CategorieDB:
                len_option = len(option.categorie_name)

            elif type(option) is Product:
                len_option = len(option.product_name_fr)

            elif type(option) is str:
                len_option = len(option)

            if len_option > max_length:
                max_length = len_option

        return max_length



    def create_menu_from_dict(self, options_dict):
        """Create a menu using a list of options
        
        options_dict : dict of the options of the menu"""

        self.options = options_dict
        self.num_options = len(options_dict)



    def change_language(self, language):
        """Change the language in conf.json if it is necessary
        language : language chosen by the user (string)"""

        #We try to open conf.json in reading mode to read its content
        try:
            with open("conf.json", "r", encoding="utf-8") as file:
                file_loaded = json.load(file)
                file.close()
                
        #If the file couldn't be opened
        except:
            print("Couldn't open file : conf.json")

        #If the language in conf.json is different from the one selected by the user
        if file_loaded["language"] != "language":
            
            try:
                with open("conf.json", "w", encoding="utf-8") as file:

                        file_loaded["language"] = language
                        file_loaded = json.dumps(file_loaded, indent=4)
                        file.write(file_loaded)
                        file.close()
            except:
                print("Couldn't open file : conf.json")



    def display(self):
        """Display the options of the menu in the terminal
        
        self.options : dictionary containing options of the menu { num_opt : option}"""

        #If there is only one option, it will be a string object
        if type(self.options) is str:
            print(self.options)
            
        else:

            max_length_options = self.calculate_max_length_options()
            #We display the - that will forme a table around the menu

            self.display_tiret(max_length_options)
            #We display each option one by one
            for option in self.options:
                if type(self.options[option]) is str:
                    print("| "+option+"."+self.options[option], end="")
                    self.display_tiret_endline(self.options[option], max_length_options)

                #If we want a menu from a dict with Categorie Object
                elif type(self.options[option]) is CategorieDB:
                    print("| "+option+"."+self.options[option].categorie_name, end="")
                    self.display_tiret_endline(self.options[option].categorie_name, max_length_options)

                #If we want a menu from a dict with Product Object
                elif type(self.options[option]) is Product:
                    print("| "+option+"."+self.options[option].product_name_fr+" : barcode: "+self.options[option].barcode, end="")
                    self.display_tiret_endline(self.options[option].product_name_fr, max_length_options)

            #We display the - that will forme a table around the menu          
            self.display_tiret(max_length_options)



    def display_tiret(self, max_length_options):
        """Display tiret on the terminal depending on the size of the longest option string
        
        max_length_options : length of the option with the longest string (int)"""

        for i in range(0, max_length_options+5):
            print("-", end="")
        print("")

    

    def display_tiret_endline(self, option, max_length_options):
        """Display the tiret at the end of the line of the menu calculating the number of space
        necessary between the option and the tiret that will form the table around the menu.
        
        option : string containing the current option
        max_length_options : size of the longest option (int)"""

        for i in range(0, max_length_options-len(option)):
            print(" ", end="")

        print("|")


    def get_options_from_json(self, menu_name):
        """Get the options to display from language.json

        menu_name : name of the menu we are looking for in language.json"""

        #We try to open language.json to get the options of the menu
        try:
            with open("language.json", encoding="utf-8") as menu_json_file:
                menu_json = json.load(menu_json_file)
                menu_json_file.close()
                return menu_json[self.language][menu_name]

        except:
            print("Couldn't open file : language.json")

    

    def input(self):
        """Display the menu while the user hasn't chosen the right option"""
        menu_input = 0

        #While the user chose the wrong main menu, we display it again
        while int(menu_input) < 1 or int(menu_input) > self.num_options:
            self.display()
            menu_input = input("=> ")
            os.system("clear")

        return menu_input


    def search_language_used(self):
        """Search in language.json in which language the menu must be displayed
        It returns the language used (fr or en)"""

        #We try to open conf.json to get the language
        try:
            with open("conf.json", encoding="utf-8") as language_json_file:
                json_lang = json.load(language_json_file)
                language_json_file.close()
                return json_lang["language"]
            
        except:
            print("Couldn't open file : conf.json")




                
            

        
