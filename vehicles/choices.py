from django.db import models


class VehicleTypeChoices(models.TextChoices):
    TRUCK = 'Truck', 'Truck'
    VAN = 'Van', 'Van'
    CAR = 'Car', 'Car'