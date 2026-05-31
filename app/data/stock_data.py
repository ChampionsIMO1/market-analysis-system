import yfinance as yf

# Get price for ticker
def fetch_stock_price(ticker: str):
    stock = yf.Ticker(ticker)
    price = stock.info.get["regularMarketPrice"]
    
    if price is None:
        raise ValueError(f"No data for: {ticker}")
    
    return price