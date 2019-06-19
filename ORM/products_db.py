# coding : utf-8

class Products_DB:
    """Allow to insert data into the Products table in openfoodfacts database"""

    def __init__(self, product_name_fr, url):
        self.product_name_fr = product_name_fr
        self.url = url