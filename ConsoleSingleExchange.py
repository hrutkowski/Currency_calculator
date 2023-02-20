from ErrorChecker import ErrorChecker
from DataGetter import DataGetter

class ConsoleSingleExchange():
    def run(self, displayManager):
        errorChecker = ErrorChecker()
        dataGetter = DataGetter()
        again = True
        while(again):
            displayManager.displayAskCurrency()
            currency = input("Currency: ")
            displayManager.displayAskDate()
            date = input("Date (YYYY-MM-DD): ")
            if(errorChecker.checkWeekday(date)=="weekend"):
                displayManager.displayErrorWeekend(date)
            elif(errorChecker.checkWeekday(date)=="holiday"):
                displayManager.displayErrorHoliday(date)
            else:
                exchange = dataGetter.getExchangeRate(currency, date)
                displayManager.displayExchange(currency, date, exchange)
            displayManager.displayAskAgain()
            choice = input("Your choice: ")
            if(choice == "0"):
                again = False
            elif(choice == "1"):
                pass
            else:
                displayManager.displayOptionError()
                again = False
            