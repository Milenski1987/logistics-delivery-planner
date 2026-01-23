from django.urls import path, include
from vehicles import views

app_name = 'vehicles'

urlpatterns = [
    path('', views.vehicles_list, name='list'),
    path('<int:pk>/', views.vehicle_details, name='details')
]