import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',     # Change if your MySQL host is different
            user='root',          # Replace with your MySQL username
            password='yourpassword' # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close cursor and connection
        if connection:
            cursor.close()
            connection.close()

# Run the function
if __name__ == "__main__":
    create_database()
