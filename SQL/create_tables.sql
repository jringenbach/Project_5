CREATE DATABASE IF NOT EXISTS openfoodfacts;

USE openfoodfacts;

CREATE TABLE IF NOT EXISTS Store(
id_store INT AUTO_INCREMENT PRIMARY KEY,
name_store VARCHAR(30) NOT NULL UNIQUE
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Brand(
id_brand INT AUTO_INCREMENT PRIMARY KEY,
brand_tags VARCHAR(80) NOT NULL UNIQUE)
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

CREATE TABLE IF NOT EXISTS ProductBrand(
barcode VARCHAR(20),
id_brand INT
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE ProductBrand
ADD CONSTRAINT fk_barcode_brand FOREIGN KEY (barcode) REFERENCES Product(barcode),
ADD CONSTRAINT fk_id_brand FOREIGN KEY (id_brand) REFERENCES Brand(id_brand);

CREATE TABLE IF NOT EXISTS ProductStore(
barcode VARCHAR(20),
id_store INT
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE ProductStore
ADD CONSTRAINT fk_barcode_store FOREIGN KEY (barcode) REFERENCES Product(barcode),
ADD CONSTRAINT fk_id_store FOREIGN KEY (id_store) REFERENCES Store(id_store);


CREATE TABLE IF NOT EXISTS ProductCategorie(
barcode VARCHAR(20),
id_categorie INT
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE ProductCategorie
ADD CONSTRAINT fk_barcode_categorie FOREIGN KEY (barcode) REFERENCES Product(barcode),
ADD CONSTRAINT fk_id_categorie FOREIGN KEY(id_categorie) REFERENCES Categorie(id_categorie);