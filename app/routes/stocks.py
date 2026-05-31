from fastapi import APIRouter
from app.services.stock_service import get_stocks_data

router = APIRouter()

# Create router for /stocks with data for all tickers listed
@router.get("/stocks")
def stocks(tickers: str):
    return get_stocks_data(tickers)