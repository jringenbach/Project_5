ALTER TABLE Products_Brands
DROP FOREIGN KEY fk_id_products_brands,
DROP FOREIGN KEY fk_id_brands;

ALTER TABLE Products_Nutrition_grade
DROP FOREIGN KEY fk_id_products_nutrition_grade,
DROP FOREIGN KEY fk_id_nutrition_grade;

ALTER TABLE Products_Categories
DROP FOREIGN KEY fk_id_products_categories,
DROP FOREIGN KEY fk_id_categories;

DROP TABLE IF EXISTS Products_Brands;

DROP TABLE IF EXISTS Products_Nutrition_grade;

DROP TABLE IF EXISTS Products_Categories;

DROP TABLE IF EXISTS Brands;

DROP TABLE IF EXISTS Categories;

DROP TABLE IF EXISTS Nutrition_grade;

DROP TABLE IF EXISTS Products;
