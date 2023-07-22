-- creates table unique_id
-- columns id int with default value 1 and must be unique
-- name varchar(256)

CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
