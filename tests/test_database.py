import pytest # import pytest, which is a testing framework for Python that allows you to write test cases and run them easily.

from database import get_connection, create_table, save_prices, count_rows, get_summary #import the necessary functions from the database module that will be tested in this file.


@pytest.fixture #marks conn as a fixture, which means it can be used as an argument in test functions to provide a fresh database connection for each test.
def conn():
    """Give each test a fresh, empty database that only exists in memory."""
    connection = get_connection(":memory:")
    create_table(connection)
    yield connection
    connection.close()


def test_new_table_is_empty(conn):# Test that a new database table is empty by asserting that the count of rows is zero.
    assert count_rows(conn) == 0


def test_save_prices_adds_one_row_per_coin(conn): # Test that saving prices adds one row per coin by saving two coins and asserting that the count of rows is two.
    save_prices(conn, {"bitcoin": 50000, "ethereum": 2000}, "gbp")
    assert count_rows(conn) == 2


def test_summary_calculates_lowest_highest_and_average(conn): # Test that the summary calculation works correctly by saving two prices for bitcoin and asserting that the summary returns the correct readings, lowest, highest, and average values.
    save_prices(conn, {"bitcoin": 100}, "gbp")
    save_prices(conn, {"bitcoin": 300}, "gbp")
    rows = get_summary(conn)
    assert rows == [("bitcoin", 2, 100, 300, 200)]