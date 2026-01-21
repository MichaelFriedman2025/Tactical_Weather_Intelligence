from mysql.connector.connection import MySQLConnectionAbstract 


def insert_to_db(data,connection:MySQLConnectionAbstract):
    cursor = connection.cursor(dictionary=True)
    sql = "INSERT INTO records_weather (timestamp,location_name,country,latitude,longitude,temperature,wind_speed,humidity ,temperature_category,wind_category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for record in data:
        val = (record["timestamp"],
               record["location_name"],
               record["country"],
               record["latitude"],
               record["longitude"],
               record["temperature"],
               record["wind_speed"],
               record["humidity"])
        
data = [{'timestamp': '2026-01-27 07:00:00', 'location_name': 'Tel Aviv', 'country': 'Israel', 'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 17.5, 'wind_speed': 13.4, 'humidity': 76},
    {'timestamp': '2026-01-27 08:00:00', 'location_name': 'Tel Aviv', 'country': 'Israel', 'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 17.6, 'wind_speed': 15.0, 'humidity': 73},
    {'timestamp': '2026-01-27 09:00:00', 'location_name': 'Tel Aviv', 'country': 'Israel', 'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 17.7, 'wind_speed': 15.5, 'humidity': 71},
    {'timestamp': '2026-01-27 10:00:00', 'location_name': 'Tel Aviv', 'country': 'Israel', 'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 18.0, 'wind_speed': 13.2, 'humidity': 70},
    {'timestamp': '2026-01-27 11:00:00', 'location_name': 'Tel Aviv', 'country': 'Israel', 'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 18.2, 'wind_speed': 10.8, 'humidity': 69},
    {'timestamp': '2026-01-27 12:00:00', 'location_name': 'Tel Aviv', 'country': 'Israel', 'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 18.4, 'wind_speed': 10.9, 'humidity': 69}, 
    {'timestamp': '2026-01-27 13:00:00', 'location_name': 'Tel Aviv', 'country': 'Israel', 'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 18.2, 'wind_speed': 12.8, 'humidity': 70}, 
    {'timestamp': '2026-01-27 14:00:00', 'location_name': 'Tel Aviv', 'country': 'Israel', 'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 17.9, 'wind_speed': 14.8, 'humidity': 72}]

    
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