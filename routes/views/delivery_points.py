from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def delivery_point_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'routes/delivery-point-add-page.html')

def delivery_points_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'routes/delivery-points-list-page.html')

def delivery_point_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'routes/delivery-point-details-page.html')

def delivery_point_edit(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'routes/delivery-point-edit-page.html')

def delivery_point_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'routes/delivery-point-delete-page.html')
