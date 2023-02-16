class DisplayManager:
    def displayMenu(self):
        print("CURRENCY CALCULATOR by Hubert Rutkowski")
    def displayAskCurrency(self):
        print("Please pick the currency that you want.")
    def displayAskDate(self):
        print("Please pick the date that intrest you. Provide it in format YYYY-MM-DD.")
    def displayExchange(self, currency, date, exchange):
        print(f"1 {currency} = {exchange} PLN in {date}")
    def displayErrorWeekend(self, date):
        print(f"{date} is a weekend date. There is no exchange data from weekends.")
    def displayErrorHoliday(self, date):
        print(f"{date} is a holiday date. There is no exchange data from holidays.")