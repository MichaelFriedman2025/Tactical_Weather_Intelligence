from fastapi import FastAPI


app = FastAPI()

@app.post("/ingest")
def stam():
    pass