# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Own classes and libraries
from Classes.brand import Brand
from Classes.nutrition_grade import Nutrition_grade


#Python libraries
import requests

class Product:
    """Define a product as it is defined in openfoodfacts"""

    def __init__(self, code, product_name_fr, url, nutrition_grade, brands):

        self.code = code
        self.product_name_fr = product_name_fr
        self.url = url
        self.nutrition_grade = Nutrition_grade(nutrition_grade)
        self.brands = Brand(brands)

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def about_me(self):
        """Print on the terminal information about the product itself"""
        try:
            print("Product name : "+self.product_name_fr)
            print("url : "+self.url)
            self.nutrition_grade.about_me()
            self.brands.about_me()
        
        except UnicodeEncodeError as unicode_encode_error:
            print("Unicode Encode Error")

    

    def find_duplicates_in_list(self, list_products):
        """Find if the product already exists in a list"""

        for product in list_products:
            if self.is_equal(product):
                list_products.remove(product)


    def is_equal(self, other_product):
        """Test if this product is equal to an other product. Return True if equal, else it returns False"""

        if self.product_name_fr == other_product.product_name_fr and \
        self.url == other_product.url:
            return True

        else:
            return False



    def set_attributes(self,product_name_fr, url):
        """Set attributes of a product"""

        self.product_name_fr = product_name_fr
        self.url = url




