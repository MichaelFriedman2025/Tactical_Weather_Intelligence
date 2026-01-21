from mysql.connector.connection import MySQLConnectionAbstract 


def insert_to_db(data,connection:MySQLConnectionAbstract):
    sql = "INSERT INTO records_weather (timestamp,location_name,country,latitude,longitude,temperature,wind_speed,humidity ,temperature_category,wind_category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (data)
    
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