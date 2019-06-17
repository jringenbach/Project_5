# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Python libraries
import requests

class Products:
    """Define a product as it is defined in openfoodfacts"""

    def __init__(self, product_name_fr, url):
        self.product_name_fr = product_name_fr
        self.url = url

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def about_me(self):
        """Print on the terminal information about the product itself"""

        print("Product name : "+self.product_name_fr)
        print("url : "+self.url)



    def set_attributes(self,product_name_fr, url):
        """Set attributes of a product"""

        self.product_name_fr = product_name_fr
        self.url = url



