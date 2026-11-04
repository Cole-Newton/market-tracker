# Market Tracker

A Python command-line app that collects live cryptocurrency prices from the CoinGecko API, stores them in a SQLite database, and produces summary reports using SQL.

This is the first project in a series I'm building around stock and crypto market data, working towards a market recap Telegram bot.

## Features

- Fetches live prices for multiple coins (Bitcoin, Ethereum, Solana) in GBP from a public REST API
- Saves every reading to a SQLite database with a UTC timestamp, building up a price history over time
- Generates a summary report per coin: number of readings, lowest, highest and average price
- Uses parameterised SQL queries to protect against SQL injection
- Handles API errors and timeouts, and closes database connections safely

## Tech stack

- **Python 3.13**
- **requests** for calling the CoinGecko REST API
- **SQLite** (Python's built-in `sqlite3`) for storage
- **SQL** for querying and aggregating the data
- **Git & GitHub** for version control

## Project structure

```
market-tracker/
├── main.py           # Fetches live prices, displays them and saves them to the database
├── database.py       # Database functions: connect, create table, save prices, run queries
├── report.py         # Prints a summary report of the stored price history
├── requirements.txt  # Python packages the project needs
└── README.md
```

## Getting started

1. Clone the repository:
   ```
   git clone https://github.com/Cole-Newton/market-tracker.git
   cd market-tracker
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # macOS / Linux
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Collect prices (run this a few times to build up a history):
   ```
   python main.py
   ```
5. View the summary report:
   ```
   python report.py
   ```

## Example output

```
Coin        Readings        Lowest       Highest       Average
--------------------------------------------------------------
Bitcoin            6     57,459.00     57,492.00     57,473.00
Ethereum           6      1,696.17      1,698.05      1,697.41
Solana             6         69.18         69.34         69.29
```

## What I learned

- Calling a REST API and handling JSON responses in Python
- Designing a database table and writing SQL to insert and aggregate data
- Structuring a project into functions and separate modules
- Using virtual environments and managing dependencies
- A Git workflow of small, focused commits

## Planned improvements

- Collect prices automatically on a schedule
- Track percentage price changes over time
- Add automated tests
- Visualise price history with charts (next project: Market Analysis)

## Licence

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.