# coding : utf-8

class CategorieDB:
    """Allow to insert data in Categories table in openfoodfacts database
    id_categorie : unique identifier of the categories (int)
    categorie_name : name of the categories (str)
    nb_categorie : number of Categories_DB instanciated (int)"""

    nb_categorie = 0
    def __init__(self, id_categorie, categorie_name):
        CategorieDB.nb_categorie += 1

        #If id_categorie is null, we set id_categorie to the nth Categories_DB instanciated
        if id_categorie is None:
            self.id_categorie = CategorieDB.nb_categorie
        else:
            self.id_categorie = id_categorie
            
        self.categorie_name = categorie_name
        
