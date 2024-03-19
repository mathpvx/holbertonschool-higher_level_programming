-- create user with password and handles the case if it exists alrdy
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL privileges ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;