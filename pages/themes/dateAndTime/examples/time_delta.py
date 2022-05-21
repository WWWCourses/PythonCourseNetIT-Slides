from datetime import datetime

# calculate time interval
t1 = datetime.strptime("08:30", "%H:%M")
t2 = datetime.strptime("12:15", "%H:%M")
print(t2 - t1)