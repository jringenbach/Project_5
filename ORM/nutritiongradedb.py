# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------
#My own libraries and classes
from Classes.nutritiongrade import Nutritiongrade

#Python libraries and classes
from sqlalchemy.exc import IntegrityError
import records


class NutritiongradeDB:
    """Allow to insert datas in Nutrition_grade table in openfoodfacts database
    nutrition_grade : name of the nutrition grade (str)"""

    def __init__(self, nutrition_grade):

        self.nutrition_grade = nutrition_grade.nutrition_grade


#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------


    def about_me(self):
        """Print in the terminal the nutrition grade"""
        print("Nutrition grade : "+self.nutrition_grade)



    def check_if_already_in_database(self, db):
        """Check if this nutrition grade already is in the database
        db : records.Connexion object"""

        select_query = "SELECT nutrition_grade FROM nutritiongrade WHERE nutrition_grade=\'"\
        +self.nutrition_grade+"\';"

        result = db.query(select_query)



    def insert_to_database(self, db):
        """Insert this nutrition grade to the database
        db : records.Connexion Object"""

        insert_query = "INSERT INTO nutritiongrade VALUES (\'"+self.nutrition_grade+"\');"

        #We try to insert this nutrition grade in the database
        try:
            db.query(insert_query)

        #If the primary key already exists
        except IntegrityError:
            print(self.nutrition_grade+" is already in database.")