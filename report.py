from database import get_connection, get_summary


def main():
    conn = get_connection()
    try:
        rows = get_summary(conn)
    finally:
        conn.close()

    if not rows:
        print("No prices saved yet. Run main.py first.")
        return

    print(f"{'Coin':<10}{'Readings':>10}{'Lowest':>14}{'Highest':>14}{'Average':>14}")
    print("-" * 62)
    for coin, readings, lowest, highest, average in rows:
        print(f"{coin.title():<10}{readings:>10}{lowest:>14,.2f}{highest:>14,.2f}{average:>14,.2f}")


if __name__ == "__main__":
    main()