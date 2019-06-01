import requests


def get_uah_usd_rate():
    try:
        response = requests.get(
            "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=3").json()
        for rate in response:
            if rate.get("ccy") == "USD" and rate.get("base_ccy") == "UAH":
                return None, round(float(rate["sale"]), 4)
        return LookupError("No USD data"), None
    except Exception as error:
        return error, None


print(get_uah_usd_rate())
