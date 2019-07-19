# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Own libraries
from ORM.branddb import BrandDB
from ORM.categoriedb import CategorieDB
from ORM.nutritiongradedb import NutritiongradeDB
from ORM.productdb import ProductDB
from ORM.productbranddb import ProductbrandDB
from ORM.productcategoriedb import ProductcategorieDB
from ORM.productstoredb import ProductstoreDB
from ORM.storedb import StoreDB
from Classes.categorie import Categorie
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
        self.connexion = self.set_database_url("conf.json")
        self.db = records.Database(self.connexion)



#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------



    def execute_sql_script_from_file(self, file_path):
        """Execute a sql script read from a file to the database
        file_path : path to the sql script that we want to read (str)"""

        #We read the sql script
        sql_script = read_txt.get_text_from_file(file_path)
        sql_script = sql_script.split("\n\n")
        print("Reading the SQL script")

        i = 0
        for script in sql_script:
            i += 1
            print("Executing script number "+str(i))
            self.db.query(script)



    def insert_datas_to_database(self, data_dict):
        """Insert data into the database"""



    def link_classes_to_orm(self, openfoodfacts_dict):
        """Instanciate ORM classes from data classes in openfoodfacts
        
        openfoodfacts_dict : dictionary that contains all categories and their products (dict)"""


        #For each categorie, we will set the classes from the ORM in order to insert everything in the database
        for categorie in openfoodfacts_dict["categories"]:
            categoriedb_to_insert = CategorieDB(categorie)
            categoriedb_to_insert.insert_to_database(self.db)
            categoriedb_to_insert.find_id_categorie_in_database(self.db)
            for product in categorie.products:
                
                #We instanciate a NutritiongradeDB object to insert into database
                nutritiongradedb_to_insert = NutritiongradeDB(product.nutrition_grade)
                nutritiongradedb_to_insert.insert_to_database(self.db)

                #We instanciate a productdb object to insert into database
                productdb_to_insert = ProductDB()
                productdb_to_insert.set_productdb_from_product(product)
                insert_successful = productdb_to_insert.insert_to_database(self.db)


                #If we succeeded to insert a product, we can insert the table that are linked to it
                if insert_successful:
                    #We instanciate a BrandDB object
                    for brand in product.brands:
                        branddb_to_insert = BrandDB(brand)
                        branddb_to_insert.insert_to_database(self.db)
                        #We instanciate a ProductbrandDB object
                        productbranddb_to_insert = ProductbrandDB(productdb_to_insert.barcode, branddb_to_insert.brand_tags)
                        productbranddb_to_insert.insert_to_database(self.db)

                    #We instanciate a storeDB object
                    for store in product.stores:
                        storedb_to_insert = StoreDB(store)
                        storedb_to_insert.insert_to_database(self.db)
                        storedb_to_insert.find_id_store_in_database(self.db)

                        #We instanciate a ProductstoreDB object
                        productstoredb_to_insert = ProductstoreDB(product.barcode, storedb_to_insert.id_store)
                        productstoredb_to_insert.insert_to_database(self.db)

                    #We instanciate a ProductcategorieDB object
                    productcategoriedb_to_insert = ProductcategorieDB(product.barcode, categoriedb_to_insert.id_categorie)
                    productcategoriedb_to_insert.insert_to_database(self.db)








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



    def get_list_of_products_from_database(self, product_name):
        """Set the product from a select query to the database with the name of the product we 
        are looking for"""

        select_query = "SELECT * FROM Product WHERE product_name_fr LIKE '%"+product_name+"%'"
        result = self.db.query(select_query)
        result.all()
        i = 0
        for product in result:
            print(result[i])
            i += 1

    
    def get_dict_of_categories_from_database(self):
        """Return the dict of the categories that are in the database
        
        dict_of_categories : dictionary containing categories { num_cat : categorie_object}"""

        dict_of_categories = dict()
        select_query = "SELECT * FROM Categorie ORDER BY categorie_name ASC;"
        result = self.db.query(select_query)
        result.all()

        for i in range(0, len(result)):
            dict_of_categories.update({str(i+1) : Categorie(result[i]["categorie_name"])})

        return dict_of_categories
            






