import requests

from database import get_connection, create_table, save_prices, count_rows

API_URL = "https://api.coingecko.com/api/v3/simple/price"
COINS = ["bitcoin", "ethereum", "solana"]
CURRENCY = "gbp"


def fetch_prices(coins, currency):
    """Get the current price of each coin from the CoinGecko API."""
    params = {"ids": ",".join(coins), "vs_currencies": currency}
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return {coin: data[coin][currency] for coin in coins if coin in data}


def show_prices(prices):
    """Print each coin's price in a readable format."""
    for coin, price in prices.items():
        print(f"{coin.title()}: £{price:,}")


def main():
    prices = fetch_prices(COINS, CURRENCY)
    show_prices(prices)

    conn = get_connection()
    try:
        create_table(conn)
        save_prices(conn, prices, CURRENCY)
        print(f"Saved to database. Total records: {count_rows(conn)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()