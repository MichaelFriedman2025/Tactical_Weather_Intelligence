from fastapi import APIRouter
from models import *


router = APIRouter()

@router.post("/records")
def post_records():
    pass


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

