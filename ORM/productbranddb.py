# coding : utf-8

class ProductbrandDB:
    """Table that connects a product to its brand
    Allow to insert data in Products_Brands table in the database
    
    id_products : unique identifier of a product (int)
    id_brands : unique identifier of a brand (int)"""

    def __init__(self, id_products, id_brands):
        self.id_products = id_products
        self.id_brands = id_brands