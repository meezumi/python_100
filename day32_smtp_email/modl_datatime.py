import datetime as dt

now = dt.datetime.now()
# this gives current date and time
year = now.year
# print(now)
month = now.month
day_of_week = now.weekday()
print(day_of_week)

dob = dt.datetime(year=2002, month=8, day=19)
print(dob)