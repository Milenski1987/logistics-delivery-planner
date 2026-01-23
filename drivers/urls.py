from django.urls import path, include
from drivers import views

app_name = 'drivers'

urlpatterns = [
    path('', views.drivers_list, name='list'),
    path('<int:pk>/', views.driver_details, name='details')
]