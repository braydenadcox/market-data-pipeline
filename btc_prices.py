import requests
from datetime import datetime

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

def main():
    try:
        price = fetch_btc_price()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"BTC Price: ${price} (as of {timestamp})")
    except requests.RequestException as e:
        print(f"Error fetching BTC price: {e}")

if __name__ == "__main__":
    main()