from pydantic import BaseModel

class Records(BaseModel):
    record: list[dict]
