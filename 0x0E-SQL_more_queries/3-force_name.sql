-- create table force_name if it doesn't exist.
-- table contains id and name columns

CREATE TABLE IF NOT EXISTS force_name (
    id INT, 
    name VARCHAR(256) NOT NULL
);
