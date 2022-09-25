DROP DATABASE IF EXISTS books_db;
CREATE DATABASE books_db;
USE books_db;

CREATE TABLE authors (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    fname VARCHAR(250) DEFAULT NULL,
    lname VARCHAR(250) NOT NULL,
    birth_year SMALLINT(4) DEFAULT NULL,
    death_year SMALLINT(4) DEFAULT NULL,
    INDEX(lname(10)),
    PRIMARY KEY (id)
);

CREATE TABLE books (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    author_id INT UNSIGNED NOT NULL,
    book_name VARCHAR(250) NOT NULL,
    pub_year SMALLINT(4) UNSIGNED DEFAULT NULL,
    INDEX(book_name(10)),
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES authors (id)
);
