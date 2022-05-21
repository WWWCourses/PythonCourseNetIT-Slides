import datetime

def get_user_bdate():
  pass

  return (bmonth, bday)

def calc_days_untill_birthdate(bmonth, bday): 
  today_date = datetime.date.today()
  today_year = today_date.year

  birthdate_this_year = datetime.date(today_year, bmonth, bday)

  delta =  birthdate_this_year - today_date

  return delta.days

if __name__ == "__main__":
  # execute only if run as a script
  bmonth = 6
  bday = 12
  days_untill_birthdate = calc_days_untill_birthdate(bmonth, bday)

  print(days_untill_birthdate)
