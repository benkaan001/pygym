import mysql.connector
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
password = os.getenv("PASSWORD")


def get_connection():
    connection = mysql.connector.connect(
        host='localhost', database='hospital_db', user='root', password=password)
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version()")
        db_version = cursor.fetchone()
        print("Connected to SQL version:", db_version)
    except (Exception, mysql.connector.Error) as error:
        print("Ups! We have an error: ", error)


print("Database version")
read_database_version()

# Database version
# Connected to SQL version: ('8.0.30',)
