CREATE DATABASE IF NOT EXISTS 'login1'
USE 'login1'

CREATE TABLE 'accounts' (
    id INT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(250) NOT NULL
);
