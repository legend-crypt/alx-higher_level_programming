-- create database htbn_0d_usa 
-- create table states in htbn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
       	name VARCHAR(256)
);
