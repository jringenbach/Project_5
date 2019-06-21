# coding : utf-8

#Own libraries
import read_txt

#Python libraries
import json
import mysql.connector
import records



class LinkDB:
    """Contains information to connect to the database
    
    DATABASE_URL : URL used to connect to the MySQL Database"""



    def __init__(self):
        self.DATABASE_URL = str()



    def execute_sql_script_from_file(self, file_path):
        """Execute a sql script read from a file to the database
        file_path : path to the sql script that we want to read (str)"""

        #We try to create the connexion to the database
        connexion = self.set_database_url("conf.json")
        db = records.Database(connexion) #Reading DATABASE_URL

        #We read the sql script
        sql_script = read_txt.get_text_from_file(file_path)
        sql_script = sql_script.split("\n\n")
        print("Reading the SQL script")

        i = 0
        for script in sql_script:
            i += 1
            print("Executing script number "+str(i))
            db.query(script)



    def insert_datas_to_database(self, data_dict):
        """Insert data into the database"""



    def link_classes_to_orm(self, openfoodfacts_dict):
        """Instanciate ORM classes from data classes in openfoodfacts"""
        list_categorie_db = list()
        list_products_db = list()
        list_nutrition_grade_db = list()
        list_brands_db = list()

        for categorie in openfoodfacts_dict["categories"]:
            categorie.about_me()
            for product in categorie.products:
                product.about_me()





    def set_database_url(self, file_path):
        """Connects a user to the database by reading its connexion information in a json configuration file.

        file_name : path and name of the json configuration file
        """

        #We open the configuration file to get the user information
        with open(file_path) as json_data:
            
                connexion = None

                #We load the json file
                connexion_info = json.load(json_data)

                #We get the user information
                host_db = connexion_info["connexion_info"]["host"]
                database_db = connexion_info["connexion_info"]["database"]
                user_db = connexion_info["connexion_info"]["user"]
                password_db = connexion_info["connexion_info"]["password"]

                self.DATABASE_URL="mysql+mysqlconnector://"+user_db+":"+password_db+"@"+host_db+":3306/openfoodfacts?charset=utf8"
                return self.DATABASE_URL







