import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='yourpassword'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Handle MySQL-specific errors
        print(f"MySQL Error: {e}")

    except Exception as e:
        # Handle other errors
        print(f"Error: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
