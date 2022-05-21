import datetime

# get current datetime:
datetime_now = datetime.datetime.today()
print("Current datetime: ",datetime_now)

# get current date
date_now = datetime.date.today()
# or:
# date_now = datetime.datetime.today().date()
print("Current date: ",date_now)

# get current time
time_now = datetime.datetime.today().time()
print("Current time: ",time_now)
