-- creates a table called first_table in the current database
CREATE TABLE IF NOT EXISTS first_table(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL,
    PRIMARY KEY (id)
);