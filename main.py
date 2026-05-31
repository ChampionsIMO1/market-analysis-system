from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Market System Running!"}

@app.get("/stocks/{ticker}")
def get_stock(ticker :str):
    stock = yf.Ticker(ticker)
    price = stock.info["regularMarketPrice"]
    return {
        "ticker": ticker.upper(),
        "price": price,
        "timestamp": "Now",
    }