import re
from datetime import date

from django.core.validators import MinLengthValidator, URLValidator, RegexValidator, MaxValueValidator
from django.db import models

from drivers.validators import driver_years_validator


# Create your models here.
class Driver(models.Model):
    full_name = models.CharField(
        max_length= 50
    )

    date_of_birth = models.DateField(
        validators=[
            driver_years_validator
        ]
    )

    phone_number = models.CharField(
        max_length=10
    )

    driving_license_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(r'^[A-Z0-9]{10}$',
                           "Driving Licence must contain exactly 10 uppercase alphanumeric characters")
        ],
        unique=True
    )

    years_of_experience = models.PositiveSmallIntegerField()

    is_active = models.BooleanField(
        default=True
    )

    @property
    def driver_age(self):
        current_year = date.today().year
        return current_year - self.date_of_birth.year

    def __str__(self):
        return f'Name: {self.full_name} - {self.driver_age} years old, with {self.years_of_experience} years experience'

