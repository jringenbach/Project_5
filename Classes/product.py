# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Own classes and libraries
from Classes.brand import Brand
from Classes.nutritiongrade import Nutritiongrade


#Python libraries
import requests


class Product:
    """Define a product as it is defined in openfoodfacts
    barcode : barcode of the product (str)
    product_name : name of the product (str)
    url : url where we can consult the product on openfoodfacts (str)
    nutrition_grade : nutriscore of the product (str)
    brand : brand of the product (Brand Object)"""

    def __init__(self, barcode, product_name_fr, url, nutrition_grade, brand):

        self.barcode = barcode
        self.product_name_fr = product_name_fr
        self.url = url
        self.nutrition_grade = Nutritiongrade(nutrition_grade)
        self.brands = Brand(brand)

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def about_me(self):
        """Print on the terminal information about the product itself"""
        try:
            print("Barcode : "+self.barcode)
            print("Product name : "+self.product_name_fr)
            print("url : "+self.url)
            self.nutrition_grade.about_me()
            self.brands.about_me()
        
        except UnicodeEncodeError as unicode_encode_error:
            print("Unicode Encode Error")

    

    def find_duplicates_in_list(self, list_products):
        """Find if the product already exists in a list
        list_products : list of the products (list)"""

        for product in list_products:
            if self.is_equal(product):
                list_products.remove(product)


    def is_equal(self, other_product):
        """Test if this product is equal to an other product. Return True if equal, else it returns False
        other_product : Product Object that we compare to this product"""

        if self.barcode == other_product.barcode and \
        self.product_name_fr == other_product.product_name_fr and \
        self.url == other_product.url:
            return True

        else:
            return False



    def set_attributes(self, product_name, url):
        """Set attributes of a product
        product_name : Name of the product (str)"""

        self.product_name = product_name
        self.url = url




