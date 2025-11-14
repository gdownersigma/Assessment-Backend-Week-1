"""Functions for working with dates."""

from datetime import datetime, date


def convert_to_datetime(date_val: str) -> datetime:
    """Converts a date string into a datetime."""
    try:
        return datetime.strptime(date_val,"%d.%m.%Y")
    except:
        raise ValueError("Unable to convert value to datetime.")


def get_days_between(first: datetime, last: datetime) -> int:
    """Find the number of days between two dates"""
    if not isinstance(first,datetime) or not isinstance(last,datetime):
        raise TypeError('Datetimes required.')
    return abs((first-last).days)


def get_day_of_week_on(date_val: datetime) -> str:
    """Returns the day of the week of a specific date."""
    if not isinstance(date_val,datetime):
        raise TypeError("Datetime required.")
    day_names= {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',
                4:'Friday',5:'Saturday',6:'Sunday'}
    return day_names[date_val.weekday()]


def get_current_age(birthdate: date) -> int:
    pass
