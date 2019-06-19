# coding : utf-8

class Products_Categories_DB:
    """Table that connects a product to its brand
    Allow to insert data in Products_Categories table in the database
    
    id_products : unique identifier of a product
    id_categorie : unique identifier of a categorie"""

    def __init__(self, id_products, id_categorie):
        self.id_products = id_products
        self.id_categorie = id_categorie