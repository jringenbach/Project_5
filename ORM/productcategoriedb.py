# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#My own libraries and classes
from Classes.categorie import Categorie
from Classes.product import Product

#Python libraries and classes
import records
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError


class ProductcategorieDB:
    """Table that connects a product to its brand
    Allow to insert data in Products_Categories table in the database
    
    barcode : barcode of the product (str)
    id_categorie : Identifier of the categorie (int)"""

    def __init__(self, barcode, id_categorie):
        self.barcode = barcode
        self.id_categorie = id_categorie

    

    def find_categorie_in_database(self, db, categorie):
        """Find a categorie in the database looking by its name
        db : a records.Connecion object
        categorie : a Categorie Object (Categorie)"""

        select_query = "SELECT id_categorie FROM categorie WHERE categorie_name='"+categorie.categorie_name+"';"
        result = db.query(select_query)
        print(result[0]["id_categorie"])

        return result[0]["id_categorie"]



    def insert_to_database(self, db):
        """Insert this ProductcategorieDB into the database"""

        #We try to insert this productcategorie into the database
        try:
            insert_query = "INSERT INTO productcategorie (barcode, id_categorie) VALUES ('"\
            +self.barcode+"', "+str(self.id_categorie)+");"
            db.query(insert_query)

        except IntegrityError as int_err:
            print("There was an integrity error while inserting productcategoriedb")
            print(int_err)

        except ProgrammingError as prg_err:       
            print("There was a programming error while inserting a productcategoriedb")

    def set_barcode(self, product):
        """Set the barcode of the product to this ProductcategorieDB"""

        self.barcode = product.barcode



    def set_id_categorie(self, db, categorie):
        """Set the id of this ProductcategorieDB
        db : a records.Connexion object"""

        self.id_categorie = self.find_categorie_in_database(db, categorie)



