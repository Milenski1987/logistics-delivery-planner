from django.contrib import admin
from drivers.models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'date_of_birth', 'phone_number', 'driving_license_number']
    list_filter = ['years_of_experience']
    search_fields = ['full_name', 'driving_license_number', 'phone_number']
    list_per_page = 20
