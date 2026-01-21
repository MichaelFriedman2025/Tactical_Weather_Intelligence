from fastapi import APIRouter
from models import *
from schemas import Records
from db import get_connection

router = APIRouter()

@router.post("/records")
def post_records(record:Records):
    conn = get_connection()
    insert_to_db(record.record,conn)
    return {"hi":"hi from service c"}

@router.get("/records")
def get_records(time_or_location:str):
    if "/" in time_or_location or "." in time_or_location or "-" in time_or_location:
        return TimeAndArea.get_record_by_time()
    else:
        return TimeAndArea.get_record_by_location()

@router.get("/records/count")
def get_the_number_of_most_info_on_country():
    return MostGroup.most_search()

@router.get("/records/avg-temperature")
def get_avg_temp():
    return AVGTemperature.avg_temp()

@router.get("/records/max-wind")
def get_max_wind():
    return MAXWind.max_wind()

@router.get("/records/extreme")
def get_most_dangerous_operations():
    return Extreame.dangerous_operations()


a = "2026/12"
b = a.split("/")
for i in b:
    print(i.isdigit())
