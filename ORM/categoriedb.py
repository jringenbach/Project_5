# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------


import records


class CategorieDB:
    """Allow to insert data in Categories table in openfoodfacts database
    categorie_name : name of the categories (str)"""

    def __init__(self, categorie_object):
            
        self.categorie_name = categorie_object.categorie_name


#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------
    


    def insert_to_database(self, db):
        """Insert categories data into database
        db : records.Database Object"""

        print("Inserting "+self.categorie_name+" to database.")
        db.query("INSERT INTO categorie (categorie_name) VALUES (:categorie_name)", \
        categorie_name=self.categorie_name)



        
