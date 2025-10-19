"""
MySQLServer.py
Creates a MySQL database named 'alx_book_store' if it does not already exist.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (adjust host, user, password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure the connection is closed properly
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
