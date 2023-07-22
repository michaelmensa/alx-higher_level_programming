-- script that creates db hbtn_0d_usa and table cities
-- cities should contain
-- id int, auto generated, can't be null, primary key
-- name varchar(256) not null
-- state_id int, can't be null, foreign key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256),
    PRIMARY KEY(id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
