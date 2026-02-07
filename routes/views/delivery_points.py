from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from common.forms import SearchForm
from routes.forms.delivery_points import DeliveryPointDeleteForm, DeliveryPointAddForm, DeliveryPointEditForm
from routes.models import DeliveryPoint


def delivery_point_add(request: HttpRequest) -> HttpResponse:
    form = DeliveryPointAddForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            delivery_point = form.save()

            return redirect('routes:delivery_point_details', pk=delivery_point.id)

    context = {
        'form': form,
        'title': 'Delivery Point',
        'back_url': 'routes:delivery_points_list',
        'icon': 'images/delivery_point_icon.png'
    }

    return render(request, 'shared/base-add-page.html', context)

def delivery_points_list(request: HttpRequest) -> HttpResponse:
    delivery_points = DeliveryPoint.objects.all()
    form = SearchForm(request.GET or None)

    if request.method == "GET":
        if form.is_valid():
            search_by = form.cleaned_data['search']
            delivery_points = DeliveryPoint.objects.filter(
                Q(name__icontains=search_by)
                |
                Q(address__icontains=search_by)
                |
                Q(city__icontains=search_by)
            )

    context={
        'delivery_points':delivery_points,
        'form': form
    }
    return render(request, 'routes/delivery-points-list-page.html', context)

def delivery_point_detail(request: HttpRequest, pk: int) -> HttpResponse:
    delivery_point = get_object_or_404(DeliveryPoint, pk=pk)

    context = {
        'delivery_point':delivery_point,
        'title': 'Delivery Point',
        'icon': 'images/delivery_point_icon.png'
    }
    return render(request, 'routes/delivery-point-details-page.html', context)

def delivery_point_edit(request: HttpRequest, pk: int) -> HttpResponse:
    delivery_point = get_object_or_404(DeliveryPoint, pk=pk)
    form = DeliveryPointEditForm(
        request.POST or None,
        instance=delivery_point
    )

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('routes:delivery_point_details', pk=pk)

    context = {
        'form': form,
        'title': 'Delivery Point',
        'id': delivery_point.id,
        'back_url': 'routes:delivery_point_details',
        'icon': 'images/delivery_point_icon.png'
    }

    return render(request, 'shared/base-edit-page.html', context)

def delivery_point_delete(request: HttpRequest, pk: int) -> HttpResponse:
    delivery_point = get_object_or_404(DeliveryPoint, pk=pk)
    form = DeliveryPointDeleteForm(
        request.POST or None,
        instance=delivery_point
    )

    if request.method == 'POST':
        if form.is_valid():
            delivery_point.delete()

            return redirect('routes:delivery_points_list')

    context = {
        'form': form,
        'title': 'Delivery Point',
        'id': delivery_point.id,
        'back_url': 'routes:delivery_point_details',
        'icon': 'images/delivery_point_icon.png'
    }

    return render(request, 'shared/base-delete-page.html', context)
