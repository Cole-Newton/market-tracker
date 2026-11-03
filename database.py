import sqlite3
from datetime import datetime, timezone

DB_PATH = "prices.db"


def get_connection(db_path=DB_PATH):
    """Open a connection to the SQLite database file (it's created if it doesn't exist)."""
    return sqlite3.connect(db_path)


def create_table(conn):
    """Create the prices table if it doesn't already exist."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coin TEXT NOT NULL,
            price REAL NOT NULL,
            currency TEXT NOT NULL,
            collected_at TEXT NOT NULL
        )
        """
    )
    conn.commit()


def save_prices(conn, prices, currency):
    """Insert one row per coin, all stamped with the same time (UTC)."""
    collected_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rows = [(coin, price, currency, collected_at) for coin, price in prices.items()]
    conn.executemany(
        "INSERT INTO prices (coin, price, currency, collected_at) VALUES (?, ?, ?, ?)",
        rows,
    )
    conn.commit()


def count_rows(conn):
    """Return how many price records are stored."""
    return conn.execute("SELECT COUNT(*) FROM prices").fetchone()[0]