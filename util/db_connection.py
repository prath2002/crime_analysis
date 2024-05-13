import mysql.connector
from mysql.connector import Error
from exception.my_exceptions import DatabaseConnectionError
from util.db_property_util import PropertyUtil


class DBConnection:
    @staticmethod
    def get_connection():
        connection = None
        try:
            connection_string = PropertyUtil.get_property_string()  # Get the connection string

            connection = mysql.connector.connect(**connection_string)
            if connection.is_connected():
                print("Database connection established successfully")
        except Error as e:
            # Raise custom exception
            raise DatabaseConnectionError("Error connecting to the database:", e)
        return connection
