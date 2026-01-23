from django.urls import path, include
from routes import views

app_name = 'routes'

assignment_urls = [
    path('add/', views.assignment_add, name='assignment_add'),
    path('', views.assignment_list, name='assignment_list'),
    path('<int:pk>/', include([
        path('', views.assignment_detail, name='assignment_details'),
        path('edit/', views.assignment_edit, name='assignment_edit'),
        path('delete/', views.assignment_delete, name='assignment_delete')
    ]))
]

routes_urls = [
    path('add/', views.route_add, name='route_add'),
    path('', views.routes_list, name='routes_list'),
    path('<int:pk>/', include([
        path('', views.route_detail, name='route_details'),
        path('edit/', views.route_edit, name='route_edit'),
        path('delete/', views.route_delete, name='route_delete')
    ]))
]

delivery_points_urls = [
    path('add/', views.delivery_point_add, name='delivery_point_add'),
    path('', views.delivery_points_list, name='delivery_points_list'),
    path('<int:pk>/', include([
        path('', views.delivery_point_detail, name='delivery_point_details'),
        path('edit/', views.delivery_point_edit, name='delivery_point_edit'),
        path('delete/', views.delivery_point_delete, name='delivery_point_delete')
    ]))
]

urlpatterns = [
    path('assignment/', include(assignment_urls)),
    path('routes/', include(routes_urls)),
    path('delivery-points/', include(delivery_points_urls))
]