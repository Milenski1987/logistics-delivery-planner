from django.urls import path
from vehicles import views


app_name = 'vehicle'

urlpatterns = [
    path('', views.VehicleListView.as_view(), name='list'),
    path('<int:pk>/', views.VehicleDetailView.as_view(), name='details')
]