from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from drivers.forms import DriverSearchAndSortForm
from drivers.models import Driver

def driver_details(request: HttpRequest, pk: int) -> HttpResponse:
    driver = get_object_or_404(Driver, pk = pk)
    context = {
        "driver": driver,
        'title': 'Driver',
        'icon': 'images/driver_icon.png'
    }
    return render(request, 'drivers/driver-details-page.html', context)

def drivers_list(request: HttpRequest) -> HttpResponse:
    form = DriverSearchAndSortForm(request.GET or None)
    drivers = Driver.objects.all()

    if request.method == 'GET':
        if form.is_valid():
            search_by = form.cleaned_data['search']
            sort_by = form.cleaned_data['sort']

            drivers = Driver.objects.filter(full_name__icontains=search_by).order_by(sort_by)

    context = {
        'drivers':drivers,
        'form': form
    }

    return render(request, 'drivers/drivers-list-page.html', context)