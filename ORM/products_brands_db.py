# coding : utf-8

class Products_Brands_DB:
    """Table that connects a product to its brand
    Allow to insert data in Products_Brands table in the database
    
    id_products : unique identifier of a product
    id_brands : unique identifier of a brand"""

    def __init__(self, id_products, id_brands):
        self.id_products = id_products
        self.id_brands = id_brands