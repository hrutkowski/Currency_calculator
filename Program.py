from DisplayManager import DisplayManager
from ConsoleExchangeTable import ConsoleExchangeTable
from ConsoleSingleExchange import ConsoleSingleExchange

class Program:
    def run(self):
        displayManager = DisplayManager()
        end = False
        while(not end):
            displayManager.displayMenu()
            option = input("Menu option number: ")
            if (option == "0"):
                end = True
            elif (option == "1"):
                consoleExchangeTable = ConsoleExchangeTable()
                consoleExchangeTable.run(displayManager)
            elif (option == "2"):
                consoleSingleExchange = ConsoleSingleExchange()
                consoleSingleExchange.run(displayManager)
            else:
                displayManager.displayOptionError()
                end = True

        



        