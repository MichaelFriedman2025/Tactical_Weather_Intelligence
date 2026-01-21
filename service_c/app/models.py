from mysql.connector.connection import MySQLConnectionAbstract 


def insert_to_db(data,connection:MySQLConnectionAbstract):
    cursor = connection.cursor()
    sql = "INSERT INTO records_weather (timestamp,location_name,country,latitude,longitude,temperature,wind_speed,humidity ,temperature_category,wind_category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for record in data:
        val = (record["timestamp"],
               record["location_name"],
               record["country"],
               record["latitude"],
               record["longitude"],
               record["temperature"],
               record["wind_speed"],
               record["humidity"],
               record["temperature_category"],
               record["wind_status"])
        cursor.execute(sql,val)
        connection.commit()

        

class TimeAndArea():

    @staticmethod    
    def get_record_by_location(location,connection:MySQLConnectionAbstract):
        cursor = connection.cursor()
        sql = "SELECT * FROM records_weather WHERE location_name like %s"
        cursor.execute(sql, (location,))
        result = cursor.fetchall()
        return result
    
    @staticmethod
    def get_record_by_time(time,connection:MySQLConnectionAbstract):
        cursor = connection.cursor()
        sql = "SELECT * FROM records_weather WHERE DateTime = %s"
        cursor.execute(sql,(time,))
        result = cursor.fetchall()
        return result

class MostGroup():

    @staticmethod
    def most_search(location,connection:MySQLConnectionAbstract):
        cursor = connection.cursor()
        sql = ""


data = [{'timestamp': '2026-01-27T23:00:00', 'location_name': 'Tel Aviv', 'country': 'Israel', 'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 17.4, 'wind_speed': 19.4, 'humidity': 56, 'temperature_category': 'cold', 'wind_status': 'windy'},{'timestamp': '2026-01-27T23:00:00', 'location_name': 'Tel Aviv', 'country': 'Israel', 'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 17.4, 'wind_speed': 19.4, 'humidity': 56, 'temperature_category': 'cold', 'wind_status': 'windy'}]
from db import get_connection
conn  = get_connection()
insert_to_db(data,conn)