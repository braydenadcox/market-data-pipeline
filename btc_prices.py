import requests
from datetime import datetime
from db import get_db_connection

def fetch_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # Raise an error for bad responses

    data = response.json()
    return float(data['bitcoin']['usd'])

def insert_btc_price(timestamp, price):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO btc_prices (timestamp, price_usd)
                VALUES (%s, %s)
                """,
                (timestamp, price)
            )

def main():
    try:
        price = fetch_btc_price()
        timestamp = datetime.now()
        insert_btc_price(timestamp, price)
        print(f"Inserted BTC price {price} at {timestamp}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()