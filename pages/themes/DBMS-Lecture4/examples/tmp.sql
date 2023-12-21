-- Active: 1663945334496@@127.0.0.1@3306@Tmp

show TABLES;

SELECT user,host FROM mysql.user;

-- DROP USER 'iva'@'localhost';

use Tmp;

CREATE TABLE IF NOT EXISTS datatypes(
  id int(10) unsigned NOT NULL AUTO_INCREMENT,
  tinyint_data tinyint(4) DEFAULT NULL,
  smallint_data smallint(6) DEFAULT NULL,
  mediumint_data mediumint(9) DEFAULT NULL,
  int_data int(11) DEFAULT NULL,
  bigint_data bigint(20) DEFAULT NULL,
  PRIMARY KEY (id)
);

INSERT INTO datatypes (tinyint_data,smallint_data,mediumint_data,int_data,bigint_data )
VALUES (100, 20000, 3000000, 100000000, 10000000000000000 );

SELECT * FROM datatypes;

ALTER TABLE datatypes ADD decimal_data DECIMAL(6,2);
ALTER TABLE datatypes ADD datetime_data DATETIME;
ALTER TABLE datatypes ADD ts_data TIMESTAMP;

INSERT INTO datatypes (datetime_data, ts_data) VALUES (
	'2023/12/21 17:32:20',
	'2023/12/21 17:32:20'
);

SELECT * FROM datatypes;