from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from routes.forms.delivery_points import DeliveryPointDeleteForm, DeliveryPointAddForm, DeliveryPointEditForm
from routes.models import DeliveryPoint


def delivery_point_add(request: HttpRequest) -> HttpResponse:
    form = DeliveryPointAddForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            delivery_point = form.save()

            return redirect('routes:delivery_point_details', pk=delivery_point.id)

    context = {
        'form': form
    }

    return render(request, 'routes/delivery-point-add-page.html', context)

def delivery_points_list(request: HttpRequest) -> HttpResponse:
    delivery_points = DeliveryPoint.objects.all()

    context={
        'delivery_points':delivery_points
    }
    return render(request, 'routes/delivery-points-list-page.html', context)

def delivery_point_detail(request: HttpRequest, pk: int) -> HttpResponse:
    delivery_point = get_object_or_404(DeliveryPoint, pk=pk)

    context = {
        'delivery_point':delivery_point
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
        'delivery_point': delivery_point
    }

    return render(request, 'routes/delivery-point-edit-page.html', context)

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
        'form': form
    }

    return render(request, 'routes/delivery-point-delete-page.html', context)
