import datetime

def get_next_sunday_date(bdate, period):	
	"""get_next_sunday_date
	
	Args:
	    bdate (datetime): Object representing the date
	    period (tuple): (start_year,end_year) interval to look into
	
	Returns:
	    list: years, on which a date will be on Sunday
	"""
	years = []

	for y in range(*period):		
		bdate_weekday = datetime.date(y, bdate.month, bdate.day).weekday()

		if bdate_weekday == 6:
			years.append(y)			

	return years


birth_date = datetime.datetime.strptime("31/12/00", "%d/%m/%y")

sundays_years = get_next_sunday_date(birth_date, (2018,2100))
print(sundays_years)