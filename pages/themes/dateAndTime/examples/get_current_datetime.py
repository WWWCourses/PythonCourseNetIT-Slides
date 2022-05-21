import datetime

# returns naive datetime object
datetime_today = datetime.datetime.today()

# equivalent to datetime.today(), when no tzinfo object is passed
datetime_now = datetime.datetime.now()

# returns the UTC time
datetime_utc = datetime.datetime.utcnow()

print(datetime_today)
print(datetime_now)
print(datetime_utc)


