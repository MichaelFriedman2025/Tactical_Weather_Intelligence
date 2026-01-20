import mysql.connector 
from mysql.connector.connection import MySQLConnectionAbstract 


def get_connection():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root")
    return mydb

def creat_database_and_table(mydb:MySQLConnectionAbstract):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE mydatabase")
    mycursor.execute("USE mydatabase;")
    mycursor.execute("""
    CREATE TABLE records_weather (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    timestamp DATETIME, 
                    location_name VARCHAR(100),
                    country VARCHAR(100), 
                    latitude FLOAT,
                    longitude FLOAT,
                    temperature FLOAT, 
                    wind_speed FLOAT, 
                    humidity INT ,
                    temperature_category VARCHAR(100), 
                    wind_category VARCHAR(100))""")