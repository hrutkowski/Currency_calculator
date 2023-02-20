class DisplayManager:
    def displayMenu(self):
        print("\n\nCURRENCY CALCULATOR by Hubert Rutkowski")
        print("\nType \"1\" to open the Exchange Table Menu.")
        print("Type \"2\" to open the Single Currency Menu.")
        print("Type \"0\" to EXIT.")
    def displayMenuTable(self):
        print("\n\nEXCHANGE TABLE MENU")
    def displayAskCurrency(self):
        print("\n\nPlease pick the currency.")
    def displayAskDate(self):
        print("\n\nPlease pick the date that intrest you. Provide it in format YYYY-MM-DD.")
    def displayExchange(self, currency, date, exchange):
        print(f"1 {currency} = {exchange} PLN in {date}")
    def displayErrorWeekend(self, date):
        print(f"{date} is a weekend date. There is no exchange data from weekends.")
    def displayErrorHoliday(self, date):
        print(f"{date} is a holiday date. There is no exchange data from holidays.")
    def displayOptionError(self):
        print("\nWRONG INPUT! There is no option like this!")
    def displayAskTableLetter(self):
        print("\nPick the table that your are intrested with:")
        print("A - Table of average foreign exchange rates")
        print("B - Table of average rates of inconvertible currencies")
    def displayAskAgain(self):
        print("\n\nType \"1\" if you want to check again.")
        print("Type \"0\" to go back to Menu.")
    def displayDataTable(self, tableDataList):
        print("\n\nCurrency    Rate:")
        for tableData in tableDataList:
            print(tableData.currency + "     ->   " + tableData.rate)
    def displayNoData(self):
        print("\nSorry there is no data in database, try something else.")