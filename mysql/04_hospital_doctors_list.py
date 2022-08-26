import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
password = os.getenv("PASSWORD")


def create_connection():
    connection = mysql.connector.connect(
        host='localhost', user='root', password=password, database='hospital_db')
    return connection


def get_doctors(hospital_id):
    try:
        connection = create_connection()
        cursor1 = connection.cursor()
        query = f"SELECT hospital_name FROM hospital WHERE hospital_id = {hospital_id}"
        cursor1.execute(query)
        # Printing doctor list for ('Mayo Clinic',) hospital  ---- Prints as tuple without further destructuring
        hospital_name = cursor1.fetchone()[0]

        cursor2 = connection.cursor()
        query = """SELECT d.doctor_name
                    FROM hospital h
                    INNER JOIN doctor d
                    ON h.hospital_id = d.hospital_id
                    WHERE h.hospital_id = %s
                    """
        cursor2.execute(query, (hospital_id,))
        records = cursor2.fetchall()
        # print(records)  # [('David',), ('Michael',)]
        print(f'Printing doctor list for "{hospital_name}" hospital')
        for [doctor] in records:
            print("Doctor Name: ", doctor)

    except (Exception, mysql.connector.Error) as error:
        print('We have an error: ', error)
    finally:
        connection.close()


get_doctors(1)

"""
Printing doctor list for "Mayo Clinic" hospital
Doctor Name:  David
Doctor Name:  Michael

"""
