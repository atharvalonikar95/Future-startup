class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        date_obj = datetime.datetime(year, month, day)
        weekday_index = date_obj.weekday()
        

        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        return weekdays[weekday_index]