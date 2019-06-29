# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError
import records


class BrandDB:
    """Allow to insert data in brands table in openfoodfacts database
    brand_object : Brand Object from Classes (Brand)    """

    def __init__(self, brand_object):

        self.brand_tags = brand_object.brand_tags

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------



    def insert_to_database(self, db):
        """Insert into database this brand
        db : records.Connexion object"""
        
        #We try to insert this brand into the database
        try:
            db.query("INSERT INTO brand (brand_tags) VALUES (:brand_tags)", brand_tags=self.brand_tags)

        #If the primary key for this brand already exists
        except IntegrityError:
            print(self.brand_tags+" : This brand is already in database.")

        except ProgrammingError:
            print("There was a programming error while inserting brand : "+self.brand_tags)