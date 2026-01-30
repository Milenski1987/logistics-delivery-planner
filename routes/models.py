from django.db import models


class DeliveryPoint(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    address = models.CharField(
        max_length=150
    )

    city = models.CharField(
        max_length=30
    )

    description = models.TextField(
        blank=True,
        null=True
    )

class Route(models.Model):
    name = models.CharField(
        max_length= 30
    )

    start_location = models.CharField(
        max_length=30
    )

    end_location = models.CharField(
        max_length=30
    )

    distance_km = models.PositiveIntegerField()

    points_for_delivery = models.ManyToManyField(
        'DeliveryPoint',
        related_name='delivery_point_routes'
    )


class Assignment(models.Model):
    route = models.ForeignKey(
        'Route',
        null = True,
        on_delete=models.SET_NULL,
        related_name='route_assignments'
    )

    driver = models.ForeignKey(
        'drivers.Driver',
        null=True,
        on_delete=models.SET_NULL,
        related_name='driver_assignments'
    )

    vehicle = models.ForeignKey(
        'vehicles.Vehicle',
        null=True,
        on_delete=models.SET_NULL,
        related_name='vehicle_assignments'
    )

    assignment_start = models.DateField()

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
