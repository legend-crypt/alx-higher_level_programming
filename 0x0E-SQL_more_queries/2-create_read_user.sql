-- create a user_0d_2 and grant him read permission
-- because he we want to let him read only the data
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT  ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
