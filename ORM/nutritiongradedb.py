# coding : utf-8

class NutritiongradeDB:
    """Allow to insert datas in Nutrition_grade table in openfoodfacts database
    nutrition_grade : name of the nutrition grade (str)"""

    def __init__(self, nutrition_grade):

        self.nutrition_grade = nutrition_grade