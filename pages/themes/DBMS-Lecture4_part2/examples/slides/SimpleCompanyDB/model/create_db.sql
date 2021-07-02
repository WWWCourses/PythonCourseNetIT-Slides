CREATE DATABASE IF NOT EXISTS SimpleCompanyDB DEFAULT CHARACTER set utf8 default collate utf8_bin;
USE SimpleCompanyDB


-- drop all tables
DROP TABLE IF EXISTS company_employee;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS company;


-- crete tables
CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    employee_name VARCHAR(100) NOT NULL
);
CREATE TABLE company (
    company_id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    company_name VARCHAR(300) NOT NULL
);
CREATE TABLE company_employee (
    employee_id INTEGER NOT NULL,
    company_id INTEGER NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employee (employee_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (company_id) REFERENCES company (company_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    PRIMARY KEY (employee_id, company_id)
);

-- insert sample data
INSERT INTO employee (employee_name) VALUES ("Ivan Petrov");
INSERT INTO employee (employee_name) VALUES ("Maria Popova");
INSERT INTO employee (employee_name) VALUES ("Georgi Ivanov");

INSERT INTO company (company_name) VALUES ("Google");
INSERT INTO company (company_name) VALUES ("Facebook");

INSERT INTO company_employee (employee_id, company_id) VALUES (1,2);
INSERT INTO company_employee (employee_id, company_id) VALUES (2,1);
INSERT INTO company_employee (employee_id, company_id) VALUES (3,1);
INSERT INTO company_employee (employee_id, company_id) VALUES (3,2);

