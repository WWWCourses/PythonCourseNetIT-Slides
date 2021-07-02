INSERT INTO a( b_id, a_filed) values
( (SELECT b_id FROM b WHERE b_field="some_value"), "a_filed_value");


insert into book(author_id,book_name) values
((SELECT id FROM author WHERE lname="Vonnegut"), "Some Vonnegut's book"),
((SELECT id FROM author WHERE lname="Vonnegut"), "Some Vonnegut's book222"),


SET @alaba = (SELECT id FROM author WHERE lname="Vonnegut");
insert into book(author_id,book_name) values
    (@authorID, "Some Vonnegut's book 1")
~~~~
INSERT INTO table1 ( column1 )
SELECT  col1
FROM    table2
