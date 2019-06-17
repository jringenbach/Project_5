# coding : utf-8

#Python library
import json

class Menu:
    """Handles menus of the program and all their methods"""



    def __init__(self, menu_name):
        """Initialization of a menu"""
        self.language = self.search_language_used()
        self.options = self.get_options_from_json(menu_name)



#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------



    def display(self):
        """Display the options of the menu in the terminal"""

        if type(self.options) is str:
            print(self.options)
            
        else:
            #We display each option one by one
            for option in self.options:
                print(option)



    def get_options_from_json(self, menu_name):
        """Get the options to display from language.json

        menu_name : name of the menu we are looking for in language.json"""

        #We try to open language.json to get the options of the menu
        try:
            with open("language.json") as menu_json_file:
                menu_json = json.load(menu_json_file)
                menu_json_file.close()
                return menu_json[self.language][menu_name]

        except:
            print("Couldn't open file : language.json")



    def search_language_used(self):
        """Search in language.json in which language the menu must be displayed
        It returns the language used (fr or en)"""

        #We try to open conf.json to get the language
        try:
            with open("conf.json") as language_json_file:
                json_lang = json.load(language_json_file)
                language_json_file.close()
                return json_lang["language"]
            
        except:
            print("Couldn't open file : conf.json")




                
            

        
