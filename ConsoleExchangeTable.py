from ErrorChecker import ErrorChecker
from DataGetter import DataGetter
from DisplayManager import DisplayManager

class ConsoleExchangeTable():
    def run(self, displayManager):
        errorChecker = ErrorChecker()
        dataGetter = DataGetter()
        again = True
        while(again):
            displayManager = DisplayManager()
            displayManager.displayMenuTable()
            displayManager.displayAskTableLetter()
            tableType = input("Table letter: ")
            if(errorChecker.checkTable(tableType) == "Error"):
                displayManager.displayOptionError()
                again = False
            else:
                displayManager.displayAskDate()
                date = input("Date (YYYY-MM-DD): ")
                if(errorChecker.checkWeekday(date) == "weekend"):
                    displayManager.displayErrorWeekend(date)
                elif(errorChecker.checkWeekday(date) == "holiday"):
                    displayManager.displayErrorHoliday(date)
                else:
                    tableDataList = dataGetter.getExchangeTable(date, tableType)
                    if (tableDataList == "No data"):
                        displayManager.displayNoData()
                    else:
                        displayManager.displayDataTable(tableDataList)
                displayManager.displayAskAgain()
                choice = input("Your choice: ")
                if(choice == "0"):
                    again = False
                elif(choice == "1"):
                    pass
                else:
                    displayManager.displayOptionError()
                    again = False
