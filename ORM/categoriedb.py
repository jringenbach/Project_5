# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Python libraries
import records
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError



class CategorieDB:
    """Allow to insert data in Categories table in openfoodfacts database
    categorie_name : name of the categories (str)
    id_categorie : The id of this categorie"""

    def __init__(self, categorie_object, id_categorie=None):
            
        self.id_categorie = id_categorie
        self.categorie_name = categorie_object.categorie_name.lower()


#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------
    


    def insert_to_database(self, db):
        """Insert categories data into database
        db : records.Database Object"""
        
        self.remove_bad_characters()
        print("Inserting "+self.categorie_name+" to database.")
        db.query("INSERT INTO categorie (categorie_name) VALUES (:categorie_name)", \
        categorie_name=self.categorie_name)



    def find_id_categorie_in_database(self, db):
        """Find the id of this categorie in the database and set self.id_categorie
        db : records.Database Object"""

        try:
            select_query = "SELECT id_categorie FROM categorie WHERE categorie_name='"+self.categorie_name+"';"
            result = db.query(select_query)
            self.id_categorie = result[0]["id_categorie"]


        except IntegrityError as int_err:
            print("There was an integrity error while selecting id categorie")
            print(int_err)

        except ProgrammingError as prg_err:
            print("There was a programming error while selecting id categorie")
            print(prg_err)



    def remove_bad_characters(self):
        """Remove characters that we don't want in the categorie name"""

        self.categorie_name = self.categorie_name.replace("\n", "")


        
