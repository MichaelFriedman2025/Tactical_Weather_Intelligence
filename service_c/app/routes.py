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
def return_the_number_of_records_by_region():
    pass

@router.get("/records/avg-temperature")
def a():
    pass

@router.get("/records/max-wind")
def a():
    pass

@router.get("/records/extreme")
def a():
    pass

