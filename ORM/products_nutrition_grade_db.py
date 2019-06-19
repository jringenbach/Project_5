# coding : utf-8

class Products_Nutrition_grade_DB:
    """Table that connects a product to its Nutrition grade
    Allow to insert data in Products_Nutrition_grade table in the database
    
    id_products : unique identifier of a product
    id_nutrition_grade : unique identifier of a nutrition_grade"""

    def __init__(self, id_products, nutrition_grade):
        self.id_products = id_products
        self.id_nutrition_grade = nutrition_grade