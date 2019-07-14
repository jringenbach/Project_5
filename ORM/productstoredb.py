# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Python libraries
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError
import records



class ProductstoreDB:
    """Table that links products to stores.
    
    barcode : barcode of a product (str)
    id_store : unique identifier of a store (int)"""

    def __init__(self, barcode, id_store):
        self.barcode = barcode
        self.id_store = id_store


#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------


    def insert_to_database(self, db):
        """Insert a productstore into a productstore table in the database
        
        db : records.Connexion Object"""

        #We try to insert productstore into the database
        try:
            insert_query = "INSERT INTO productstore (barcode, id_store) VALUES ('"\
            +self.barcode+"', "+str(self.id_store)+");"
            db.query(insert_query)

        except IntegrityError as int_err:
            print("There was an integrity error while inserting productstore")
            print(int_err)

        except ProgrammingError as prg_err:
            print("There was a programming error while inserting productstore")
            print(prg_err)