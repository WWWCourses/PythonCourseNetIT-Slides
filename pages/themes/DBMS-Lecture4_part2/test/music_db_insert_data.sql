USE music_db;

INSERT INTO artist
VALUES (0,'Robert', 'Smith');


CREATE TABLE `artist` (
  `artist_id` smallint(5) AUTO_INCREMENT,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) NOT NULL,
  PRIMARY KEY (`artist_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

