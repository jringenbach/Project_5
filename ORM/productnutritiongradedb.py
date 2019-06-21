# coding : utf-8

class ProductNutritiongradeDB:
    """Table that connects a product to its Nutrition grade
    Allow to insert data in Products_Nutrition_grade table in the database
    
    id_products : unique identifier of a product (int)
    id_nutrition_grade : unique identifier of a nutrition_grade (int)"""

    def __init__(self, id_products, nutrition_grade):
        self.id_products = id_products
        self.id_nutrition_grade = nutrition_grade