from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

now = datetime.now()
timestamp = now.timestamp()

print (timestamp)

year_2023 = datetime(2023, 1, 1)

def print_date(date):
    print (date.year)
    print (date.day)
    print (date.hour)
    print (date.minute)
    print (date.second)
    print(date.timestamp())

print_date(now)

current_time = time(hour=22)

print(current_time.hour)

current_date = date(year=2024, month=8, day=3)

print(current_date)


diff = now - year_2023
print(diff)

 
time_delta = timedelta()