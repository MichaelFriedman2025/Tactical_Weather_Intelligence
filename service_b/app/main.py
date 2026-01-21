from fastapi import FastAPI
import uvicorn
import routes


app = FastAPI()

app.include_router(routes.router)


if __name__ == "__main__":
    uvicorn.run("main:app",port=8000,host="localhost" ,reload=True)