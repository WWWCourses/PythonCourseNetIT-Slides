import datetime

start_date = datetime.datetime.today()
print(start_date)

end_date = datetime.datetime.strptime("31.12.2018", "%d.%m.%Y")
print(end_date)

# td = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

td = end_date - start_date

print(td)