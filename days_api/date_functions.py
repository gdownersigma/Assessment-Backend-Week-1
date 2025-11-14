"""Functions for working with dates."""

from datetime import datetime, date


def convert_to_datetime(date_val: str) -> datetime:
    """Converts a date string into a datetime."""
    try:
        return datetime.strptime(date_val,"%d.%m.%Y")
    except:
        raise ValueError("Unable to convert value to datetime.")


def get_days_between(first: datetime, last: datetime) -> int:
    pass


def get_day_of_week_on(date_val: datetime) -> str:
    pass


def get_current_age(birthdate: date) -> int:
    pass
