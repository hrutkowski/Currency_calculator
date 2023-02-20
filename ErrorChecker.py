import datetime
import holidays

class ErrorChecker:
    def checkWeekday(self, date):
        weekday = datetime.datetime.strptime(date, "%Y-%m-%d").weekday()
        if weekday >= 5:
            return "weekend"
        
        pl_holidays = holidays.Poland()
        if datetime.date.fromisoformat(date) in pl_holidays:
            return "holiday"
    def checkTable(self, tableType):
        if((tableType != "A" and tableType !="a") and (tableType != "B" and tableType != "b")):
            return "Error"
