from datetime import datetime

def calc_days_until_birthdate(birthdate: str) -> int:
    """
    Calculates the number of days from today to the next occurrence of the birthdate.

    Parameters:
        birthdate (str): The birthdate in "DD.MM.YYYY" format.

    Returns:
        int: The number of days until the next occurrence of the birthdate.
    """
    today = datetime.now()
    birth_day, birth_month, birth_year = map(int, birthdate.split('.'))
    this_year_birthday = datetime(year=today.year, month=birth_month, day=birth_day)

    if this_year_birthday < today:
        # If this year's birthday has passed, calculate for the next year
        next_year_birthday = datetime(year=today.year + 1, month=birth_month, day=birth_day)
        delta = next_year_birthday - today
    else:
        # If this year's birthday is yet to come
        delta = this_year_birthday - today

    return delta.days

# Example usage
birthdate = "25.02.1990" # 25th February 1990
print(f"Days until next birthday: {calc_days_until_birthdate(birthdate)}")
