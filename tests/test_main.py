import main


class FakeResponse:
    """Pretends to be the reply from CoinGecko, so tests don't need the internet."""

    def __init__(self, data):
        self._data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self._data


def test_fetch_prices_returns_simple_dictionary(monkeypatch):
    fake_data = {"bitcoin": {"gbp": 50000}, "ethereum": {"gbp": 2000}}
    monkeypatch.setattr(main.requests, "get", lambda *args, **kwargs: FakeResponse(fake_data))

    prices = main.fetch_prices(["bitcoin", "ethereum"], "gbp")

    assert prices == {"bitcoin": 50000, "ethereum": 2000}


def test_fetch_prices_skips_coins_the_api_did_not_return(monkeypatch):
    fake_data = {"bitcoin": {"gbp": 50000}}
    monkeypatch.setattr(main.requests, "get", lambda *args, **kwargs: FakeResponse(fake_data))

    prices = main.fetch_prices(["bitcoin", "notarealcoin"], "gbp")

    assert prices == {"bitcoin": 50000}