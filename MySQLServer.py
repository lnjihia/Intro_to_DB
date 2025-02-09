import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server 
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password=""  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Specifically catch MySQL errors
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection if they exist
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")


# Run the function
create_database()
