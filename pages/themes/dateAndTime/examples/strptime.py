import datetime

dt = datetime.datetime.strptime("15/02/17 22:10", "%d/%m/%y %H:%M")
print(dt)
# 2017-02-15 22:10:00

bdate = datetime.datetime.strptime("18.12.31", "%y.%m.%d")
print(bdate)
# 2018-12-31 00:00:00
