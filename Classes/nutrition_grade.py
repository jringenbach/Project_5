# coding : utf-8

class Nutrition_grade:
    """Grade that represents how healthy is a product. It goes from a to e."""

    def __init__(self, nutrition_grade):
        self.nutrition_grade = nutrition_grade

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def about_me(self):
        """Print in the terminal the nutrition grade"""
        print("Nutrition grade : "+self.nutrition_grade)