-- script that creates db hbtn_0d_usa and table states
-- states should contain
-- id int, auto generated, can't be null, primary key
-- name varchar(256) not null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256),
    PRIMARY KEY(id)
);
