import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
password = os.getenv("PASSWORD")


def get_connection():
    connection = mysql.connector.connect(
        host='localhost', user='root', database='hospital_db', password=password)
    return connection


def get_hospital_detail(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT * FROM hospital WHERE hospital_id = {hospital_id}")
        h_id, h_name, bed_count = cursor.fetchone()
        print("Printing Hospital Record")
        print("Hospital Id: ", h_id)
        print("Hospital Name: ", h_name)
        print("Bed Count: ", bed_count)
    except (Exception, mysql.connector.Error) as error:
        print("Ups! We have an error: ", error)
    finally:
        connection.close()


def get_doctor_detail(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """ SELECT * FROM doctor WHERE doctor_id = %s"""
        cursor.execute(query, (doctor_id,))
        records = cursor.fetchall()
        print("Printing Doctor Record")
        for row in records:
            print("Doctor Id: ", row[0])
            print("Doctor Name: ", row[1])
            print("Hospital Id: ", row[2])
            print("Caring Since: ", row[3])
            print("Specialty:", row[4])
            print("Salary: ", row[5])
            print("Experience ", row[6])
    except (Exception, mysql.connector.Error) as error:
        print("Ups! We have an error: ", error)
    finally:
        connection.close()


print("Read given hospital and doctor details")
get_hospital_detail(2)
print("\n")
get_doctor_detail(108)

"""
Read given hospital and doctor details
Printing Hospital Record
Hospital Id:  2
Hospital Name:  Cleveland Clinic
Bed Count:  400


Printing Doctor Record
Doctor Id:  108
Doctor Name:  Karen
Hospital Id:  4
Caring Since:  2011-10-17
Specialty: Radiologist
Salary:  30000
Experience  None
"""
