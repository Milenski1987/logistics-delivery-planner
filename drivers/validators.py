from datetime import date

from django.core.exceptions import ValidationError

def driver_years_validator(value):
    current_date = date.today()
    driver_bday = value
    age = current_date.year - driver_bday.year

    if (current_date.month < driver_bday.month) or (current_date.month == driver_bday.month and current_date.day < driver_bday.day):
        age -= 1

    if age < 18:
        raise ValidationError("Driver must be at least 18 years old!")