# coding : utf-8

class ProductDB:
    """Allow to insert data into the Products table in openfoodfacts database
    id_products : unique identifier of the products (int)
    product_name_fr : name of the product (str)
    url : url where we can find the product (str)
    nb_products : number of Products_DB instanciated (int)"""

    nb_products = 0

    def __init__(self, id_products, product_name_fr, url):
        ProductDB.nb_products += 1

        #If id_products is null, we set id_products to the nth Products_DB instanciated
        if id_products is None:
            self.id_products = ProductDB.nb_products
        else:
            self.id_products = id_products
            
        self.product_name_fr = product_name_fr
        self.url = url