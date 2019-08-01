USE openfoodfacts;

ALTER TABLE ProductStore
DROP FOREIGN KEY fk_barcode_store,
DROP FOREIGN KEY fk_id_store;

ALTER TABLE ProductBrand
DROP FOREIGN KEY fk_barcode_brand,
DROP FOREIGN KEY fk_id_brand;

ALTER TABLE Product
DROP FOREIGN KEY fk_barcode_nutrition_grade;

ALTER TABLE ProductCategorie
DROP FOREIGN KEY fk_barcode_categorie,
DROP FOREIGN KEY fk_id_categorie;

ALTER TABLE RegisteredProduct
DROP FOREIGN KEY fk_barcode_product,
DROP FOREIGN KEY fk_barcode_substitute;

DROP TABLE IF EXISTS ProductStore;

DROP TABLE IF EXISTS ProductBrand;

DROP TABLE IF EXISTS ProductCategorie;

DROP TABLE IF EXISTS Brand;

DROP TABLE IF EXISTS Categorie;

DROP TABLE IF EXISTS Nutritiongrade;

DROP TABLE IF EXISTS Product;

DROP TABLE IF EXISTS Store;
