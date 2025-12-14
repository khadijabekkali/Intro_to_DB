-- Use the database (optional if passed via mysql command)
USE alx_book_store;

-- Print the full description of the 'books' table
SELECT 
    COLUMN_NAME AS 'Column',
    COLUMN_TYPE AS 'Data Type',
    IS_NULLABLE AS 'Nullable',
    COLUMN_DEFAULT AS 'Default',
    COLUMN_KEY AS 'Key',
    EXTRA AS 'Extra'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store' 
    AND TABLE_NAME = 'Books'
ORDER BY 
    ORDINAL_POSITION;
