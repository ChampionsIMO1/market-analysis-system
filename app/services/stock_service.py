from app.data.stock_data import fetch_stock_price

cache = {}

# Get all data for each ticker in the list
def get_stocks_data(tickers: str):
    ticker_list = tickers.split(",")
    results = []

    for t in ticker_list:
        t = t.strip().upper()

        try:
            if t in cache:
                price = cache[t]
            else:
                price = fetch_stock_price(t)
                cache[t] = price

            results.append({
                "ticker": t,
                "price": price,
                "timestamp": "Now",
                "status": "success",
            })

        except Exception as e:
            results.append({
                "ticker": t,
                "price": None,
                "timestamp": "Now",
                "status": "error",
                "message:": str(e),
            })

    return results