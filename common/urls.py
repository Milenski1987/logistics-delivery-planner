from django.urls import path, include

from common import views

app_name = 'common'

urlpatterns = [
    path('', views.home_page, name='home')
]