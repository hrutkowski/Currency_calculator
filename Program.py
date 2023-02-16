from DataGetter import DataGetter
from DisplayManager import DisplayManager
from DateChecker import DateChecker

class Program:
    def run(self):
        dataGetter = DataGetter()
        displayManager = DisplayManager()
        dateChecker = DateChecker()
        displayManager.displayMenu()
        displayManager.displayAskCurrency()
        currency = input("Currency: ")
        displayManager.displayAskDate()
        date = input("Date: ")
        if(dateChecker.checkWeekday(date)=="weekend"):
            displayManager.displayErrorWeekend(date)
        elif(dateChecker.checkWeekday(date)=="holiday"):
            displayManager.displayErrorHoliday(date)
        else:
            exchange = dataGetter.getExchangeRate(currency, date)
            displayManager.displayExchange(currency, date, exchange)



        