from fastapi import APIRouter ,Body
from schemas import Records
from modols import CleanData
from dotenv import load_dotenv
import requests
import os


router = APIRouter()
load_dotenv()
host=os.getenv("SERVICE_C_HOST")
port=os.getenv("SERVICE_C_PORT")


@router.post("/clean")
def clean_data(records: Records):
    data_after_clean = CleanData.main_function(records.record)
    url = f"https://{host}:{port}"
    send_to_service_c = requests.post(url, json = data_after_clean)
    return send_to_service_c.json()
    