#When will my birthday be on given weekday name

import datetime

def find_years_with_weekday(date, target_weekday, search_period):
    """Finds years within a specified period when a given date falls on a specified weekday.

    Parameters:
        birth_date (datetime.datetime): The date of interest.
        target_weekday (str): The name of the weekday to match.
        search_period (tuple): A tuple specifying the start (inclusive) and end (exclusive) years to search.

    Returns:
        list: A list of years within the search_period when birth_date falls on target_weekday.
    """
    matching_years = []
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for year in range(*search_period):
        current_date = datetime.date(year, birth_date.month, birth_date.day)
        if weekdays[current_date.weekday()] == target_weekday:
            matching_years.append(year)

    return matching_years



birth_date = datetime.datetime.strptime("31.12.2000", "%d.%m.%Y")

years_by_weekday = find_years_with_weekday(birth_date, 'Sunday', (2018,2100))
print(years_by_weekday)
