CREATE TABLE pharmacy (
id INT,
name TEXT NOT NULL,
branch TEXT NOT NULL,
address TEXT NOT NULL,
phone TEXT NOT NULL,
mail TEXT NOT NULL,
PRIMARY KEY(id)
);

CREATE TABLE users (
id INT,
name TEXT NOT NULL,
mail TEXT NOT NULL,
phone TEXT NOT NULL,
password TEXT NOT NULL,
PRIMARY KEY(id)
);

CREATE TABLE medicine (
id INT,
name TEXT NOT NULL,
description TEXT NOT NULL,
category TEXT NOT NULL,
pharmacy_id INT,
FOREIGN KEY (pharmacy_id) REFERENCES pharmacy(id),
PRIMARY KEY(id)
);