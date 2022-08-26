import mysql.connector
import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
password = os.getenv("PASSWORD")


def get_connection():
    connection = mysql.connector.connect(
        host='localhost', user='root', password=password, database='hospital_db')
    return connection


def update_doctor_experience(doctor_id):
    try:
        connection = get_connection()
        cursor1 = connection.cursor()
        update_query = """UPDATE doctor
                SET experience = ROUND( (DATEDIFF(CURDATE(), joining_date)) / 365, 1)
                WHERE doctor_id = %s"""
        cursor1.execute(update_query, (doctor_id,))
        connection.commit()

        cursor2 = connection.cursor()
        select_query = """SELECT * FROM doctor where doctor_id = %s"""
        cursor2.execute(select_query, (doctor_id,))
        records = cursor2.fetchall()
        print(
            f"Printing doctors")
        for row in records:
            print("Doctor Id: ", row[0])
            print("Doctor Name: ", row[1])
            print("Hospital Id: ", row[2])
            print("Caring Since: ", row[3])
            print("Specialty: ", row[4])
            print("Salary: ", row[5])
            print("Experience: ", row[6], "\n")

    except (Exception, mysql.connector.Error) as error:
        print("Ups! We have an error: ", error)
    finally:
        connection.close()


update_doctor_experience(104)
