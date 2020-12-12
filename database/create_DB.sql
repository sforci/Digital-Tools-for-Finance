DROP DATABASE IF EXISTS DTFF_DB;

CREATE DATABASE DTFF_DB;

USE DTFF_DB;

CREATE USER 'DTTFUser'@'localhost' IDENTIFIED BY 'DTTFPassword';

GRANT ALL PRIVILEGES ON DTFF_DB.* TO 'DTTFUser'@'localhost';

FLUSH PRIVILEGES;

CREATE TABLE people_info (
	_name VARCHAR(40),
	date_of_birth date,
	Sex CHAR(1),
	Employment_status bool);



INSERT INTO people_info (_name, date_of_birth, Sex, Employment_status) 
VALUES ('Jordan Brett Seligmann', '1996-09-26', 'M', FALSE),
		 ('Silvia Forcina Barrero', '1998-08-15', 'F', FALSE),
		 ('Filip Sprusansky', '1964-09-24','M', FALSE),
		 ('Villem Adolf Armulik', '1967-06-25', 'M', FALSE);
