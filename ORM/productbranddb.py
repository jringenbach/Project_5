# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Python libraries
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError
import records



class ProductbrandDB:
    """Table that connects a product to its brand
    Allow to insert data in Products_Brands table in the database
    
    barcode : unique identifier of a product (str)
    id_brands : unique identifier of a brand (int)"""

    def __init__(self, barcode, id_brands):
        self.barcode = barcode
        self.id_brands = id_brands

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def insert_to_database(self, db):
        """Insert into database a productbrand
        db : a records.Connexion object"""

        #We try to insert a productbrand into database
        try:
            db.query("INSERT INTO productbrand (:barcode, :id_brands) VALUES", \
            barcode=self.barcode, id_brands=self.id_brands)

        except IntegrityError as int_err:
            print("There was an integrity error while inserting a productbrand")
            print(int_err)

        except ProgrammingError:
            print("There was a programming error while inserting this productbrand")