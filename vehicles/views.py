from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def vehicles_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'vehicles/vehicles-list-page.html')

def vehicle_details(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'vehicles/vehicle-details-page.html')
