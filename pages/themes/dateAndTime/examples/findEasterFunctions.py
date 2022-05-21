def butcher_easter(year):
    "Returns Easter as a date object."
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return datetime.date(year, month, day)

def ian_taylor_easter(year):
 	"""Calculates the Easter date for given year. 
 	
 	Args:
 	    year (TYPE): Description
 	
 	Returns:
 	    TYPE: Description
 	"""
 	a = year % 19
 	b = year >> 2
 	c = b // 25 + 1
 	d = (c * 3) >> 2
 	e = ((a * 19) - ((c * 8 + 5) // 25) + d + 15) % 30
 	e += (29578 - a - e * 32) >> 10
 	e -= ((year % 7) + b - d + e + 2) % 7
 	d = e >> 5
 	day = e - d * 31
 	month = d + 3
 	return year, month, day
