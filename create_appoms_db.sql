-- A cript that creates a database if not already existing

CREATE DATABASE IF NOT EXISTS appoms_db;
USE appoms_db;
CREATE USER 'ugwu'@'localhost' IDENTIFIED BY 'Friday_123';
GRANT ALL PRIVILEGES ON 'appoms_db.*' TO 'appoms_dev'@'localhost';

