import requests
from TableData import TableData

class DataGetter:
    def getExchangeRate(self, currency, date):
        address = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date}/"
        response = requests.get(address)
        if response.status_code == 200:
            data = response.json()
            rate = data["rates"][0]["mid"]
            return rate
    def getExchangeTable(self, date, tableType):
        address = f"http://api.nbp.pl/api/exchangerates/tables/{tableType}/{date}/"
        response = requests.get(address)
        if response.status_code == 200:
            data = response.json()
            tableDataList = []
            for rate in data[0]["rates"]:
                tableData = TableData(rate["code"], rate["mid"])
                tableDataList.append(tableData)
            return tableDataList
        else:
            return "No data"
        