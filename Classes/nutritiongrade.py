# coding : utf-8

class Nutritiongrade:
    """Grade that represents how healthy is a product. It goes from a to e."""

    def __init__(self, nutrition_grade):
        self.nutrition_grade = nutrition_grade

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def about_me(self):
        """Print in the terminal the nutrition grade"""
        print("Nutrition grade : "+self.nutrition_grade)



    def find_duplicates_in_list(self, list_nutrition_grade):
        """Find if the nutrition_grade already exists in a list
        list_nutrition_grade : list of nutrition grades (list)"""

        for nutrition_grade in list_nutrition_grade:
            if self.is_equal(nutrition_grade):
                list_nutrition_grade.remove(nutrition_grade)



    def is_equal(self, other_nutrition_grade):
        """Test if this nutrition_grade is equal to an other nutrition_grade.
        Return True if equal, else it returns False
        other_nutrition_grade : Nutrition_grade Object"""

        if self.nutrition_grade == other_nutrition_grade.nutrition_grade:
            return True
        else:
            return False  