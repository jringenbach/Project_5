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
from Classes.product import Product
from Classes.store import Store
import read_txt

#Python libraries
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError

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


    def check_if_product_already_in_dict(self, prod, dict_of_products):
        """Check if the product is already in the dictionary of product we want to display. If it
        already exists, we add a store to product that already exists.
        Return True if already exists.
        
        prod : product we want to check if it already is in the dictionary (Product)"""

        for key, product in dict_of_products.items():
            if product.barcode == prod.barcode:
                product.stores.append(Store(prod.stores[0].name_store))
                return True
        
        return False


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
        
        dict_of_categories : dictionary containing categories { num_cat : CategorieDB_object}"""

        dict_of_categories = dict()
        select_query = "SELECT * FROM Categorie ORDER BY categorie_name ASC;"
        result = self.db.query(select_query)
        result.all()

        for i in range(0, len(result)):
            categorie = Categorie(result[i]["categorie_name"])
            categorie_db = CategorieDB(categorie, result[i]["id_categorie"])
            dict_of_categories.update({str(i+1) : categorie_db})

        return dict_of_categories



    def get_dict_of_products_from_database(self, id_categorie):
        """Return the dict of products depending on a categorie
        
        id_categorie : id of the categorie we want a dict of product from (int)
        dict_of_products : dict containing product => { num_product : product}
        num_product_key_dict : key of the dictionary of products that will associate a product to a menu number"""
            
        dict_of_products = dict()

        #We select a product with the categorie, store associated to it
        select_query = "SELECT Product.barcode, Product.product_name_fr, Product.url, "\
        +" Product.nutrition_grade, Store.name_store FROM Product "\
        +" LEFT JOIN Productcategorie ON Product.barcode=Productcategorie.barcode "\
        +" LEFT JOIN Categorie ON Categorie.id_categorie = Productcategorie.id_categorie "\
        +" LEFT JOIN Productstore ON Product.barcode = Productstore.barcode"\
        +" LEFT JOIN Store ON Productstore.id_store = Store.id_store"\
        +" WHERE Productcategorie.id_categorie="+str(id_categorie)\
        +" ORDER BY Product.nutrition_grade;"
        

        result = self.db.query(select_query)
        result.all()

        num_product_key_dict = 1
        #We create a dictionary of products that we will return
        for i in range(0, len(result)):
            barcode = result[i]["barcode"]
            product_name = result[i]["product_name_fr"]
            url = result[i]["url"]
            nutritiongrade_product = result[i]["nutrition_grade"]
            stores_product = result[i]["name_store"]

            prod = Product(barcode=barcode, product_name_fr=product_name, url=url, nutrition_grade=nutritiongrade_product, brands=None, stores=stores_product)
            product_already_exist_in_dict = self.check_if_product_already_in_dict(prod, dict_of_products)

            #If the product doesn't already exist in the dict, we insert it
            if product_already_exist_in_dict == False:
                dict_of_products.update({str(num_product_key_dict) : prod})
                num_product_key_dict += 1


        #Dict containing all the products from the categorie selected by the user
        return dict_of_products



    def get_list_of_product_with_better_nutrition_grade(self, dict_of_products, product_chosen):
        """Return a list of product with a better nutrition grade than the product chosen by the user
        
        dict_of_products : dictionary containing Product Object {"num_prod" : Product object}
        product_chosen : Product chosen by the user (Product)"""

        list_of_product_with_better_nutrition_grade = list()

        for key, prod in dict_of_products.items():
            if ord(prod.nutrition_grade.nutrition_grade) < ord(product_chosen.nutrition_grade.nutrition_grade):
                list_of_product_with_better_nutrition_grade.append(prod)

        return list_of_product_with_better_nutrition_grade


    def get_list_of_product_and_substitute_from_database(self):
        """Get list of the product and their substitute"""

        #We select the product the user tried to find substitution for
        select_query_product = "SELECT Product.barcode, Product.product_name_fr, Product.url, "\
        +" Product.nutrition_grade, Store.name_store, RegisteredProduct.id_registered_product"\
        +" FROM RegisteredProduct "\
        +" LEFT JOIN Product ON RegisteredProduct.barcode_product = Product.barcode"\
        +" LEFT JOIN Productcategorie ON Product.barcode=Productcategorie.barcode "\
        +" LEFT JOIN Categorie ON Categorie.id_categorie = Productcategorie.id_categorie "\
        +" LEFT JOIN Productstore ON Product.barcode = Productstore.barcode"\
        +" LEFT JOIN Store ON Productstore.id_store = Store.id_store"\
        +" ORDER BY RegisteredProduct.id_registered_product;"

        #We select the product of substitution
        select_query_substitute = "SELECT Product.barcode, Product.product_name_fr, Product.url, "\
        +" Product.nutrition_grade, Store.name_store , RegisteredProduct.id_registered_product"\
        +" FROM RegisteredProduct "\
        +" LEFT JOIN Product ON RegisteredProduct.barcode_substitute = Product.barcode"\
        +" LEFT JOIN Productcategorie ON Product.barcode=Productcategorie.barcode "\
        +" LEFT JOIN Categorie ON Categorie.id_categorie = Productcategorie.id_categorie "\
        +" LEFT JOIN Productstore ON Product.barcode = Productstore.barcode"\
        +" LEFT JOIN Store ON Productstore.id_store = Store.id_store"\
        +" ORDER BY RegisteredProduct.id_registered_product;"

        #We try to get those products from the database
        try:
            result_product = self.db.query(select_query_product)
            result_substitute = self.db.query(select_query_substitute)
            result_product.all()
            result_substitute.all()

            dict_of_product = self.get_dict_of_product_from_registered_product(result_product)
            dict_of_substitute = self.get_dict_of_product_from_registered_product(result_substitute)
            dict_product_and_substitute = {"product" : dict_of_product, "substitute" : dict_of_substitute}

            return dict_product_and_substitute
            

        except IntegrityError:
            print("There was an integrity error while getting registered product.")

        except ProgrammingError:
            print("There was a programming error while getting registered products")
        


    def get_dict_of_product_from_registered_product(self, result):
        """Turn a Record Object of product into a clean dictionary
        
        dict_of_product : dictionary {"num" : Product}"""

        list_id_registered_product = list()
        dict_of_product = dict()

        #We go through record in the result
        for record in result:
            #If we haven't already check this id registered product
            if record["id_registered_product"] not in list_id_registered_product:
                list_id_registered_product.append(record["id_registered_product"])
                barcode = record["barcode"]
                product_name_fr = record["product_name_fr"]
                url = record["url"]
                name_store = record["name_store"]
                nutrition_grade = record["nutrition_grade"]
                id_registered_product = record["id_registered_product"]

                prod = Product(barcode=barcode, product_name_fr=product_name_fr, url=url, nutrition_grade=nutrition_grade, brands=None, stores=name_store)
                
                #We create the dict of product under the form { "num" : "product"}
                dict_of_product.update({str(id_registered_product) : prod})

            #else, we add the store to the product
            else:
                name_store = record["name_store"]
                dict_of_product[str(record["id_registered_product"])].stores.append(Store(record["name_store"]))
        
        return dict_of_product









