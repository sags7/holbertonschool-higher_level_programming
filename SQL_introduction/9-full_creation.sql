-- this script creates a table second_table and adds multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT AUTO_INCREMENT,
    name VARCHAR(256),
    score INT,
    PRIMARY KEY (id)
);

INSERT INTO
    second_table
VALUES
    (1, 'John', 10);

INSERT INTO
    second_table
VALUES
    (2, 'Alex', 3);

INSERT INTO
    second_table
VALUES
    (3, 'Bob', 14);

INSERT INTO
    second_table
VALUES
    (4, 'George', 8);