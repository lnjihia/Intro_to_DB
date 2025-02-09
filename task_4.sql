-- Retrieve full description of the 'books' table without using DESCRIBE or EXPLAIN
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'books' AND TABLE_SCHEMA = DATABASE();
