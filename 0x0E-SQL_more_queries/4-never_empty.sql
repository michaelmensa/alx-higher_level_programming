-- creates table id_not_null
-- columns id int with default value 1 and must be unique
-- name varchar(256)

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
