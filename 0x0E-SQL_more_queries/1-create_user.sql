-- script that creates a MYSQL server user user_0d_1
-- user_0d_1 password is user_0d_1_pwd
-- script should not fail if user_0d_1 already exists

-- if the user does not exist, create the user and grant all privileges
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
