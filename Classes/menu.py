# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Python libraries
import json
import os


class Menu:
    """Handles menus of the program and all their methods

    language : language of the menu (str)
    options : options of the menu that will be displayed (str or dict)
    num_options : number of options in the menu (int)"""



    def __init__(self, menu_name):
        """Initialization of a menu"""
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
        """Display the options of the menu in the terminal"""

        if type(self.options) is str:
            print(self.options)
            
        else:
            #We display each option one by one
            for option in self.options:
                print(option+"."+self.options[option])



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




                
            

        
