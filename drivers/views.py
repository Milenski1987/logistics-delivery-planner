from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from drivers.models import Driver


# Create your views here.
def driver_details(request: HttpRequest, pk: int) -> HttpResponse:
    driver = Driver.objects.get(pk=pk)
    context = {
        "driver": driver
    }
    return render(request, 'drivers/driver-details-page.html', context)

def drivers_list(request: HttpRequest) -> HttpResponse:
    all_drivers = Driver.objects.all()
    context = {
        'drivers':all_drivers
    }
    return render(request, 'drivers/drivers-list-page.html', context)