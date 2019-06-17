# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Own classes and libraries
from Classes.link_api import Link_API
from Classes.products import Products

#Python libraries
import requests

class Categorie:
    """Categorie of a product.
    Example : boissons, confiserie, etc...
    
    categorie_name : name of this categorie (str)
    products: list of products for this categorie (list)"""

    def __init__(self, categorie_name):
        """categorie_name : Name of the categorie"""
        self.categorie_name = categorie_name
        self.products = list()



#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------


    def get_products_by_categorie(self):
        """Get a list of products by categorie and set self.products"""

        url = "https://fr.openfoodfacts.org/categorie/"+self.categorie_name+".json"
        #We try to request openfoodfacts to get all products from this categorie as a json
        try:
            products_json = requests.get(url).json()

        except:
            print("Couldn't request : openfoodfacts")

        #We set self.products
        self.set_products_list(products_json["products"])

    

    def set_products_list(self, products_json):
        """Set the products list for this categorie"""

        for product in products_json:
            #If the product has a product name and a nutrition grade
            if "product_name" in product.keys() and "nutrition_grades" in product.keys():
                self.products.append(Products(product["product_name"], product["url"], product["nutrition_grades"]))

        for product in self.products:
            product.about_me()



    