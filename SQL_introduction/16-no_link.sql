-- script lists all records of the table on a db in the server
-- where the name column contains a value

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
