from fastapi import APIRouter ,Query
from schemas import Records

router = APIRouter()

@router.post("/clean")
def clean_data(data:Records):
    print(data)
    return {"hi":"hi from server b"}