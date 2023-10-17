# --------------------------------- Example 1 -------------------------------- #
# from datetime import datetime, timezone

# print(f'datetme.now: {datetime.now()}')
# print(f'datetme.utcnow: {datetime.utcnow()}')
# print(f'datetime.now(timezone.utc): {datetime.now(timezone.utc)}')


# --------------------------------- Example 2 -------------------------------- #
# from datetime import datetime

# now = datetime.now()

# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# second = now.second
# microsecond = now.microsecond

# print("Year:", year)
# print("Month:", month)
# print("Day:", day)
# print("Hour:", hour)
# print("Minute:", minute)
# print("Second:", second)
# print("Microsecond:", microsecond)

# --------------------------------- Example 3 -------------------------------- #
# from datetime import datetime

# now = datetime.now()

# formatted_date = now.strftime("%d.%m.%Y")
# formatted_time = now.strftime("%H:%M:%S")

# print("Formatted Date:", formatted_date)
# print("Formatted Time:", formatted_time)

# --------------------------------- Example 4 -------------------------------- #
# from datetime import datetime

# user_birthdate_str='30.12.2000'
# user_birthdate=datetime.strptime(user_birthdate_str,"%d.%m.%Y")
# # user_birthdate_formated = datetime.strftime(user_birthdate,"%dth %B, %Y")

# print(f'user birth year: {user_birthdate.year}')
# print(f'user birth month: {user_birthdate.month}')
# print(f'user birth day: {user_birthdate.day}')

# # print(f'\nuser_birthdate_formated: {user_birthdate_formated}')

# --------------------------------- Example 5 -------------------------------- #
# from datetime import datetime, timedelta

# current_date = datetime.now().date()


# one_week_ahead = current_date + timedelta(weeks=1)
# hundred_days_before = current_date - timedelta(days=100)

# print("One week from today:", one_week_ahead)
# print("100 days before today:", hundred_days_before)

# --------------------------------- Example 6 -------------------------------- #
# from datetime import datetime, date, timedelta

# today = datetime.now().date()
# user_birthdate = date(year=2000,month=1,day=31)
# # print(user_birthdate)

# td = today - user_birthdate
# print(f'User is {td.days} days old')
# print(f'User is {td.weeks} weeks old')

# --------------------------------- Example 7 -------------------------------- #
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# # User's birthdate
# user_birthdate = datetime(year=2000, month=1, day=31)

# # Current date
# current_date = datetime.now()

# # Calculate the age difference in years, days, and minutes
# age_difference = relativedelta(current_date, user_birthdate)
# # print(age_difference)
# years = age_difference.years
# months = age_difference.months
# days = age_difference.days
# minutes = age_difference.hours * 60 + age_difference.minutes

# print(f"The user is {years} years, {months} months, {days} days, and {minutes} minutes old.")

# --------------------------------- Example 8 -------------------------------- #
# import datetime

# def get_weekday_name(date, lang):
# 	named_wd = {
# 		'bg':["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"],
# 		'en':["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# 	}

# 	wd_name = named_wd[lang][date.weekday()]
# 	return wd_name

# now = datetime.datetime.now()

# print('Днес е ', get_weekday_name(now, "bg"))
# print('Today is', get_weekday_name(now, "en"))

# --------------------------------- Example 9 -------------------------------- #
# import datetime

# def get_years_by_weekday(date, weeekday_name, period):
# 	"""get_years_by_weekday

# 	Args:
# 		date (datetime): Object representing the date
# 		period (tuple): (start_year,end_year) interval to look into

# 	Returns:
# 		list: years, on which a date will be on Sunday
# 	"""
# 	years = []

# 	for y in range(*period):
# 		date_weekday = datetime.date(y, date.month, date.day).weekday()

# 		if wd_names[date_weekday] == weeekday_name:
# 			years.append(y)

# 	return years


# wd_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# birth_date = datetime.datetime.strptime("31.12.2000", "%d.%m.%Y")

# years_by_weekday = get_years_by_weekday(birth_date, 'Sunday', (2018,2100))
# print(years_by_weekday)
# #[2023, 2028, 2034, 2045, 2051, 2056, 2062, 2073, 2079, 2084, 2090]

# -------------------------------- Example 10 -------------------------------- #
# import datetime

# def calc_easter_dates(year):
# 	"Returns Easter as a date object."
# 	a = year % 19
# 	b = year // 100
# 	c = year % 100
# 	d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
# 	e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
# 	f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
# 	month = f // 31
# 	day = f % 31 + 1

# 	return datetime.date(year, month, day)

# def calc_easter_dates_in_range(start, end):
# 	easter_dates = []
# 	for year in range(start, end+1):
# 		easter_dates.append(calc_easter_dates(year).strftime("%d.%m.%Y"))

# 	return easter_dates

# easter_dates = calc_easter_dates_in_range(2020, 2024)
# print('\n'.join(easter_dates))
# print('*'*50)

# -------------------------------- Example 11 -------------------------------- #
# from dateutil.easter import easter

# def calc_easter_dates_in_range(start, end, method):
# 	easter_dates = []
# 	for year in range(start, end+1):
# 		# easter_dates.append(calc_easter_dates(year).strftime("%d.%m.%Y"))
# 		easter_dates.append(easter(year, method=method).strftime("%d.%m.%Y"))

# 	return easter_dates


# methods = ['EASTER_JULIAN', 'EASTER_ORTHODOX', 'EASTER_WESTERN']
# for method_idx in range(len(methods)):
# 	easter_dates = calc_easter_dates_in_range(2020, 2024, method=method_idx+1)
# 	print(f'Easter dates for {methods[method_idx]}:')
# 	print('\n'.join(easter_dates))
# 	print('*'*50)

# print(easter(2023, method=1))
# print(easter(2023, method=2))
# print(easter(2023, method=3))

# -------------------------------- Example 12 -------------------------------- #
import time
from functools import reduce

#start timer
start = time.time()


# do some time intensive stuff:
num_range = (1, 10_000_000)
sum = reduce(lambda x,y:x+y, range(num_range[0],num_range[1]+1))
print(f"The sum of numbers from {num_range[0]} to {num_range[1]} is: ", sum)

#end timer
end = time.time()

print("[Finished in {:.3f}s]".format(end - start))
