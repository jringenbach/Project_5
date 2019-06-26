# coding : utf-8


#My own libraries and classes
from ORM.nutritiongradedb import NutritiongradeDB
from Classes.product import Product

#Python libraries
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError
import records


class ProductDB:
    """Allow to insert data into the Products table in openfoodfacts database
    barcode : barcode of the product (str)
    id_products : unique identifier of the products (int)
    product_name_fr : name of the product (str)
    url : url where we can find the product (str)
    nutrition_grade : Nutrition_grade Object (Represents a foreign key in database)"""


    def __init__(self, barcode=None, id_products=None, product_name_fr=None, url=None, nutrition_grade=None):
        self.barcode = barcode   
        self.product_name_fr = product_name_fr
        self.url = url
        self.nutrition_grade = nutrition_grade

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------



    def about_me(self):
        """Print on the terminal information about the product itself"""
        try:
            print("Product name : "+self.product_name_fr)
            print("url : "+self.url)
            self.nutrition_grade.about_me()
        
        except UnicodeEncodeError as unicode_encode_error:
            print("Unicode Encode Error")


    
    def insert_to_database(self, db):
        """Insert this product values into the database
        db : records.Connexion Object """

        insert_query = "INSERT INTO product (barcode, product_name_fr, url, nutrition_grade) VALUES "
        insert_query += "(\'"+self.barcode+"\', "
        insert_query += "\'"+self.product_name_fr+"\',"
        insert_query += "\'"+self.url+"\',"
        insert_query += "\'"+self.nutrition_grade.nutrition_grade+"\'"
        insert_query += ");"

        try:
            db.query(insert_query)

        except IntegrityError:
            print(self.product_name_fr+" is already in database.")

        except ProgrammingError:
            print("There was a programming error while inserting : "+self.product_name_fr)




    def set_productdb_from_product(self, product_object):
        """Set a productdb object from a product object
        product_object : A Product object"""

        self.barcode = product_object.barcode
        self.product_name_fr = product_object.product_name_fr
        self.url = product_object.url
        self.nutrition_grade = NutritiongradeDB(product_object.nutrition_grade)