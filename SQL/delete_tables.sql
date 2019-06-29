USE openfoodfacts;

ALTER TABLE ProductBrand
DROP FOREIGN KEY fk_barcode_brand,
DROP FOREIGN KEY fk_id_brand;

ALTER TABLE Product
DROP FOREIGN KEY fk_barcode_nutrition_grade;

ALTER TABLE ProductCategorie
DROP FOREIGN KEY fk_barcode_categorie,
DROP FOREIGN KEY fk_id_categorie;

DROP TABLE IF EXISTS ProductBrand;

DROP TABLE IF EXISTS ProductCategorie;

DROP TABLE IF EXISTS Brand;

DROP TABLE IF EXISTS Categorie;

DROP TABLE IF EXISTS Nutritiongrade;

DROP TABLE IF EXISTS Product;
