-- converts 'hbtn_0c_0' db to UTF-8 in MySQL Server

USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_n CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
