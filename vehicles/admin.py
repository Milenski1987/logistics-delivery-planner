from django.contrib import admin

from vehicles.models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'registration_number', 'vehicle_type', 'capacity_kg']
    list_filter = ['vehicle_type', 'capacity_kg']
    search_fields = ['make', 'registration_number']
    list_per_page = 20
