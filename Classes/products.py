# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Own classes and libraries
from Classes.brands import Brands
from Classes.nutrition_grade import Nutrition_grade

#Python libraries
import requests

class Products:
    """Define a product as it is defined in openfoodfacts"""

    def __init__(self, product_name_fr, url, nutrition_grade, brands):
        self.product_name_fr = product_name_fr
        self.url = url
        self.nutrition_grade = Nutrition_grade(nutrition_grade)
        self.brands = Brands(brands)

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def about_me(self):
        """Print on the terminal information about the product itself"""

        print("Product name : "+self.product_name_fr)
        print("url : "+self.url)
        self.nutrition_grade.about_me()
        self.brands.about_me()

    

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




