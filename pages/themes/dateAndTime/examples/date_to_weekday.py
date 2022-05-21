import datetime


def get_next_sunday_date(bdate):	
	month = bdate.month
	day = bdate.day
	years = []

	for y in range(2018, 2050):		
		bdate_weekday = datetime.date(y, month, day).weekday()

		if bdate_weekday == 6:
			years.append(y)			

	print( years )

def get_weekday_name(bdate):	
	wd_name = named_wd[bdate.weekday()]
	return wd_name

named_wd = ["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"]
bdate = datetime.date(1950, 4, 9)

y = 2002
easter = ian_taylor_easter(y)
print( easter )
