from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def driver_details(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'drivers/driver-details-page.html')

def drivers_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'drivers/drivers-list-page.html')