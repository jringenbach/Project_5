CREATE DATABASE IF NOT EXISTS openfoodfacts;

USE openfoodfacts;

CREATE TABLE IF NOT EXISTS Brands(
id_brands INT AUTO_INCREMENT PRIMARY KEY,
brands_tags VARCHAR(30) NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Nutrition_grade(
nutrition_grade VARCHAR(1) PRIMARY KEY
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Categories(
id_categories INT AUTO_INCREMENT PRIMARY KEY,
categorie_name VARCHAR(50) NOT NULL
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Products(
id_products INT AUTO_INCREMENT PRIMARY KEY,
product_name_fr VARCHAR(60) NOT NULL,
url VARCHAR(40) NOT NULL
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Products_Brands(
id_products INT,
id_brands INT
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE Products_Brands
ADD CONSTRAINT fk_id_products_brands FOREIGN KEY (id_products) REFERENCES Products(id_products),
ADD CONSTRAINT fk_id_brands FOREIGN KEY (id_brands) REFERENCES Brands(id_brands);

CREATE TABLE IF NOT EXISTS Products_Nutrition_grade(
id_products INT,
nutrition_grade VARCHAR(1)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE Products_Nutrition_grade
ADD CONSTRAINT fk_id_products_nutrition_grade FOREIGN KEY (id_products) REFERENCES Products(id_products),
ADD CONSTRAINT fk_id_nutrition_grade FOREIGN KEY(nutrition_grade) REFERENCES Nutrition_grade(nutrition_grade);

CREATE TABLE IF NOT EXISTS Products_Categories(
id_products INT,
id_categories INT
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE Products_Categories
ADD CONSTRAINT fk_id_products_categories FOREIGN KEY (id_products) REFERENCES Products(id_products),
ADD CONSTRAINT fk_id_categories FOREIGN KEY(id_categories) REFERENCES Categories(id_categories);