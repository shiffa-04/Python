import calendar
import datetime

month, day, year = map(int, input().split())

date = datetime.date(year, month, day)
day_name = calendar.day_name[date.weekday()]
print(day_name.upper())