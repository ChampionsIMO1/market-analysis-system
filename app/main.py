from fastapi import FastAPI
from app.routes import stocks

app = FastAPI()

app.include_router(stocks.router)

@app.get("/")
def root():
    return {"message": "Market System Running!"}