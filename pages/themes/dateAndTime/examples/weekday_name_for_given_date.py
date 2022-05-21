import datetime

def get_weekday_name(date):	
	named_wd = ["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"]

	wd_name = named_wd[date.weekday()]
	return wd_name

date = datetime.datetime.strptime("06/04/18", "%d/%m/%y")
print( get_weekday_name(date) )