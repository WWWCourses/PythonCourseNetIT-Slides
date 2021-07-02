DROP DATABASE IF EXISTS books_db;
CREATE DATABASE books_db;
USE books_db;

CREATE TABLE author (
    id SMALLINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
    fname VARCHAR(250) DEFAULT NULL,
    lname VARCHAR(250) NOT NULL,
    birth_year SMALLINT(4) DEFAULT NULL,
    death_year SMALLINT(4) DEFAULT NULL,
    INDEX(lname(10))
);
CREATE TABLE book (
    author_id SMALLINT(3) UNSIGNED NOT NULL,
    book_name VARCHAR(250) NOT NULL,
    pub_year SMALLINT(4) UNSIGNED DEFAULT NULL,
    INDEX(author_id(10)),
    INDEX(book_name(10)),

);
