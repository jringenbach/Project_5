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
    
    store : a Store Object coming from Classes.store"""

    def __init__(self, store):
        self.store = store


#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------


def insert_to_database(self, db):
    """Insert this store into the dabase
    
    db : a records.Connexion object"""

    #We try to insert the store into the database
    try:
        db.query("INSERT INTO store (:name_store) VALUES", name_store=self.store.name_store)

    except IntegrityError as int_err:
        print("There was an integrity error while inserting the store : "+self.store.store_name)
        print(int_err)

    except ProgrammingError as prg_err:
        print("There was a programming error while inserting the store : "+self.store.store_name)
        print(prg_err)