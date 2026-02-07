from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from vehicles.forms import VehicleSearchAndSortForm
from vehicles.models import Vehicle


# Create your views here.
def vehicles_list(request: HttpRequest) -> HttpResponse:
    vehicles = Vehicle.objects.all()
    form = VehicleSearchAndSortForm(request.GET or None)

    if request.method == 'GET':
        if form.is_valid():
            search_by = form.cleaned_data['search']
            sort_by = form.cleaned_data['sort']

            vehicles = Vehicle.objects.filter(make__icontains=search_by).order_by(sort_by)

    context = {
        'form': form,
        'vehicles': vehicles
    }

    return render(request, 'vehicles/vehicles-list-page.html', context)

def vehicle_details(request: HttpRequest, pk: int) -> HttpResponse:
    vehicle = get_object_or_404(Vehicle, pk=pk)

    context = {
        'vehicle': vehicle,
        'title': 'Vehicle',
        'icon': 'images/vehicle_icon.png'
    }

    return render(request, 'vehicles/vehicle-details-page.html', context)
