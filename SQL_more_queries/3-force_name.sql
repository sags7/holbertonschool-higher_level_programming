-- script creates a table on the MySQL server
CREATE TABLE IF NOT EXISTS force_name(
    id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
)