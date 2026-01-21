from fastapi import APIRouter, HTTPException
from services import ingest_weather_for_location
import requests
from pydantic import BaseModel


class Records(BaseModel):
    record: list[dict]

router = APIRouter()

@router.post("/ingest")
def data_ingest(location_name: str):
    try:
        data = ingest_weather_for_location(location_name)
        data1 = Records(record=data)
        url = "http://localhost:8000/clean"
        request = requests.post(url,json= data1.model_dump(mode="json"))
        return request.json()
    except:
        raise HTTPException(status_code=400, detail="the load data faild")