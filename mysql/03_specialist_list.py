import mysql.connector
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
password = os.getenv("PASSWORD")


def get_connection():
    connection = mysql.connector.connect(
        host='localhost', user='root', password=password, database='hospital_db')
    return connection


def get_specialist_list(specialty, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """SELECT * FROM doctor WHERE specialty = %s AND salary > %s"""
        cursor.execute(query, (specialty, salary))
        records = cursor.fetchall()
        print(
            f"Printing doctors whose specialty is {specialty} and salary is above ${salary}\n")
        for row in records:
            print("Doctor Id: ", row[0])
            print("Doctor Name: ", row[1])
            print("Hospital Id: ", row[2])
            print("Caring Since: ", row[3])
            print("Specialty: ", row[4])
            print("Salary: ", row[5])
            print("Experience: ", row[6], "\n")
    except (Exception, mysql.connector.Error) as error:
        print("Ups! We have an error", error)
    finally:
        connection.close()


get_specialist_list("Gynecologist", 25000)


"""
Printing doctors whose specialty is Gynecologist and salary is above $25000

Doctor Id:  105
Doctor Name:  Linda
Hospital Id:  3
Caring Since:  2004-06-04
Specialty:  Gynecologist
Salary:  42000
Experience:  None

Doctor Id:  107
Doctor Name:  Richard
Hospital Id:  4
Caring Since:  2014-08-21
Specialty:  Gynecologist
Salary:  32000
Experience:  None

"""
