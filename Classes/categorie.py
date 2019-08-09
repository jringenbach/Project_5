# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Own classes and libraries
from Classes.product import Product


#Python libraries
import requests
from requests.exceptions import HTTPError


class Categorie:
    """Categorie of a product.
    Example : boissons, confiserie, etc...
    
    categorie_name : name of this categorie (str)
    products: list of products for this categorie (list)"""

    DATABASE_URL = "https://fr.openfoodfacts.org/cgi/search.pl"

    def __init__(self, categorie_name):
        """categorie_name : Name of the categorie"""

        self.categorie_name = categorie_name.lower()
        self.products = list()



#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------


    def about_me(self):
        """Print on the terminal information about this categorie"""

        print("Categorie name : "+self.categorie_name)



    def get_products_by_categorie(self):
        """Get a list of products by categorie and set self.products"""

        params = {
            "action" : "process",
            "json" : 1,
            "tagtype_0" : "categories",
            "tag_contains_0" : "contains",
            "tag_0" : self.categorie_name,
            "page_size" : "50"
        }

        #We try to request openfoodfacts to get all products from this categorie as a json
        #We use an environment variable DATABASE_URL
        try:
            products_json = requests.get(Categorie.DATABASE_URL, params=params)
            products_json.encoding = "utf-8"
            products_json = products_json.json()
            self.set_products_list(products_json["products"])

        except HTTPError as http_err:
            print("HTTP Error : "+http_err)



    def set_products_list(self, products_json):
        """Set the products list for this categorie
        
        products_json : products in a json format"""


        for product in products_json:
            #If the product has a product name, a brand and a nutrition grade, we add it to the
            #products list
            if "product_name" in product.keys() and "nutrition_grades" in product.keys() \
            and "brands" in product.keys() and "code" in product.keys():
                self.products.append(Product(product["code"], product["product_name"], \
                product["url"], product["nutrition_grades"], product["brands"], \
                product["stores"]))



    