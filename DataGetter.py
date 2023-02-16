import requests

class DataGetter:
    def getExchangeRate(self, currency, date):
        address = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date}/"
        response = requests.get(address)
        if response.status_code == 200:
            data = response.json()
            rate = data["rates"][0]["mid"]
            return rate
        else:
            return "No info"
