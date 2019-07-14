# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#My own libraries and classes
from Classes.store import Store

#Python libraries
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError
import records



class StoreDB:
    """Class that is connected to database and allow requests about stores
    
    store : a Store Object coming from Classes.store
    id_store : Store identifier in the database (int)"""

    def __init__(self, store):
        self.id_store = None
        self.store = store


#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------



    def insert_to_database(self, db):
        """Insert this store into the dabase
        
        db : a records.Connexion object"""

        #We try to insert the store into the database
        try:
            print("*********************************************************************************")
            print(self.store.name_store)
            db.query("INSERT INTO store (name_store) VALUES (:name_store)", name_store=self.store.name_store)

        except IntegrityError as int_err:
            print("There was an integrity error while inserting the store : "+self.store.name_store)
            print(int_err)

        except ProgrammingError as prg_err:
            print("There was a programming error while inserting the store : "+self.store.name_store)
            print(prg_err)



    def find_id_store_in_database(self, db):
        """Get the id for this store from the database and set self.id_store
        db : record.Connexion Object"""

        try:
            select_query = "SELECT id_store FROM store WHERE name_store='"+self.store.name_store+"';"
            result = db.query(select_query)
            self.id_store = result[0]["id_store"]

        except IntegrityError as int_err:
            print("There was an integrity error while selecting id store")
            print(int_err)

        except ProgrammingError as prg_err:
            print("There was a programming error while selecting id store : ")
            print(prg_err)