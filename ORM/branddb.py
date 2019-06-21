# coding : utf-8

class BrandDB:
    """Allow to insert data in brands table in openfoodfacts database
    id_brands : unique identifier of the brands (int)
    brands_tags : name of the brands (str)    
    nb_brands : number of brands instanciated"""

    nb_brands = 0
    def __init__(self, id_brands, brands_tags):
        BrandDB.nb_brands += 1

        #If id_brands is null, we set the id to the nth brands_db instanciated
        if id_brands is None:
            self.id_brands = BrandDB.nb_brands
        else:
            self.id_brands = id_brands
        self.brands_tags = brands_tags