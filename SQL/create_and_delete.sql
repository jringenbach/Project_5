USE openfoodfacts;

ALTER TABLE Product_Brand
DROP FOREIGN KEY fk_barcode_brand,
DROP FOREIGN KEY fk_id_brand;

ALTER TABLE Product
DROP FOREIGN KEY fk_barcode_nutrition_grade;

ALTER TABLE Product_Categorie
DROP FOREIGN KEY fk_barcode_categorie,
DROP FOREIGN KEY fk_id_categorie;

DROP TABLE IF EXISTS Product_Brand;

DROP TABLE IF EXISTS Product_Categorie;

DROP TABLE IF EXISTS Brand;

DROP TABLE IF EXISTS Categorie;

DROP TABLE IF EXISTS Nutritiongrade;

DROP TABLE IF EXISTS Product;

CREATE TABLE IF NOT EXISTS Brand(
id_brand INT AUTO_INCREMENT PRIMARY KEY,
brand_tags VARCHAR(80) NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Nutritiongrade(
nutrition_grade VARCHAR(1) PRIMARY KEY
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Categorie(
id_categorie INT AUTO_INCREMENT PRIMARY KEY,
categorie_name VARCHAR(50) NOT NULL
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Product(
barcode VARCHAR(20) PRIMARY KEY,
product_name_fr VARCHAR(100) NOT NULL,
url VARCHAR(200) NOT NULL,
nutrition_grade VARCHAR(1) NOT NULL
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE Product
ADD CONSTRAINT fk_barcode_nutrition_grade FOREIGN KEY (nutrition_grade) REFERENCES Nutritiongrade(nutrition_grade);

CREATE TABLE IF NOT EXISTS Product_Brand(
barcode VARCHAR(20),
id_brand INT
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE Product_Brand
ADD CONSTRAINT fk_barcode_brand FOREIGN KEY (barcode) REFERENCES Product(barcode),
ADD CONSTRAINT fk_id_brand FOREIGN KEY (id_brand) REFERENCES Brand(id_brand);


CREATE TABLE IF NOT EXISTS Product_Categorie(
barcode VARCHAR(20),
id_categorie INT
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE Product_Categorie
ADD CONSTRAINT fk_barcode_categorie FOREIGN KEY (barcode) REFERENCES Product(barcode),
ADD CONSTRAINT fk_id_categorie FOREIGN KEY(id_categorie) REFERENCES Categorie(id_categorie);