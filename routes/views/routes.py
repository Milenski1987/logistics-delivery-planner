from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def route_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'routes/route-add-page.html')

def routes_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'routes/routes-list-page.html')

def route_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'routes/route-details-page.html')

def route_edit(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'routes/route-edit-page.html')

def route_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'routes/route-delete-page.html')
