# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Own classes and libraries
from Classes.nutrition_grade import Nutrition_grade

#Python libraries
import requests

class Products:
    """Define a product as it is defined in openfoodfacts"""

    def __init__(self, product_name_fr, url, nutrition_grade):
        self.product_name_fr = product_name_fr
        self.url = url
        self.nutrition_grade = Nutrition_grade(nutrition_grade)

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def about_me(self):
        """Print on the terminal information about the product itself"""

        print("Product name : "+self.product_name_fr)
        print("url : "+self.url)
        self.nutrition_grade.about_me()


    def set_attributes(self,product_name_fr, url):
        """Set attributes of a product"""

        self.product_name_fr = product_name_fr
        self.url = url




