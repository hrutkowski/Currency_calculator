import datetime
import holidays

class DateChecker:
    def checkWeekday(self, date):
        weekday = datetime.datetime.strptime(date, "%Y-%m-%d").weekday()
        if weekday >= 5:
            return "weekend"
        
        pl_holidays = holidays.Poland()
        if datetime.date.fromisoformat(date) in pl_holidays:
            return "holiday"