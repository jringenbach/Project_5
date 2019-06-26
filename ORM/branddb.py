# coding : utf-8


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

        insert_query = "INSERT INTO brand (brand_tags) VALUES (\'"+self.brand_tags+"\');"

        #We try to insert this brand into the database
        try:
            db.query(insert_query)

        #If the primary key for this brand already exists
        except IntegrityError:
            print(self.brand_tags+" is already in database.")

        except ProgrammingError:
            print("There was a programming error while inserting : "+self.brand_tags)