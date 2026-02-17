from django.contrib import admin

from routes.models import DeliveryPoint, Route, Assignment


@admin.register(DeliveryPoint)
class DeliveryPointAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'address']
    list_filter = ['city']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_location', 'end_location', 'distance_km']
    list_filter = ['start_location', 'end_location']
    search_fields = ['start_location', 'end_location']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 20

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['driver_name', 'vehicle_make', 'route_name']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['assignment_start']
    list_per_page = 20

    @staticmethod
    def driver_name(obj):
        return obj.driver.full_name if obj.driver else '-'

    @staticmethod
    def vehicle_make(obj):
        return obj.vehicle.make if obj.vehicle else '-'

    @staticmethod
    def route_name(obj):
        return obj.route.name if obj.route else '-'
