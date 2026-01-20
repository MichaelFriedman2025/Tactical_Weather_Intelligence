from fastapi import APIRouter, HTTPException
from services import resolve_city_and_send

router = APIRouter()

@router.post("/ingest")
def data_ingest(location_name: str):
    try:
        data = resolve_city_and_send(location_name)
        return { "The data": data }
    except:

        raise HTTPException(status_code=400, detail="the load data faild")