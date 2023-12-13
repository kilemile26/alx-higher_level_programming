-- script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE TABLE second_table IF NOT EXISTS (
	id INT AUTOINCREMENT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table (name, score) VALUES("John", 10), ("Alex", 3), ("Bob", 14), ("George", 8);
