from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from common.forms import SearchForm
from routes.forms.routes import RouteDeleteForm, RouteAddForm, RouteEditForm
from routes.models import Route


def route_add(request: HttpRequest) -> HttpResponse:
    form = RouteAddForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            route = form.save()

            return redirect('routes:route_details', pk=route.id)

    context = {
        'form': form,
        'title': 'Route',
        'back_url': 'routes:routes_list',
        'icon': 'images/route_icon.png'
    }

    return render(request, 'shared/base-add-page.html', context)

def routes_list(request: HttpRequest) -> HttpResponse:
    routes = Route.objects.all()
    form = SearchForm(request.GET or None)

    if request.method == 'GET':
        if form.is_valid():
            search_by = form.cleaned_data['search']
            routes = Route.objects.filter(
                Q(name__icontains=search_by)
                |
                Q(start_location__icontains=search_by)
                |
                Q(end_location__icontains=search_by)
            )

    context = {
        'routes': routes,
        'form':form
    }

    return render(request, 'routes/routes-list-page.html', context)

def route_detail(request: HttpRequest, pk: int) -> HttpResponse:
    route = get_object_or_404(Route, pk=pk)

    context = {
        'route': route,
        'title': 'Route',
        'icon': 'images/route_icon.png'
    }

    return render(request, 'routes/route-details-page.html', context)

def route_edit(request: HttpRequest, pk: int) -> HttpResponse:
    route = get_object_or_404(Route, pk=pk)
    form = RouteEditForm(
        request.POST or None,
        instance=route
    )

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('routes:route_details', pk=pk)

    context = {
        'form': form,
        'title': 'Route',
        'id': route.id,
        'back_url': 'routes:route_details',
        'icon': 'images/route_icon.png'
    }

    return render(request, 'shared/base-edit-page.html', context)

def route_delete(request: HttpRequest, pk: int) -> HttpResponse:
    route = get_object_or_404(Route, pk=pk)
    form = RouteDeleteForm(
        request.POST or None,
        instance = route
    )

    if request.method == "POST":
        if form.is_valid():
            route.delete()
            return redirect('routes:routes_list')

    context = {
        'form': form,
        'title': 'Route',
        'id':route.id,
        'back_url': 'routes:route_details',
        'icon': 'images/route_icon.png'
    }

    return render(request, 'shared/base-delete-page.html', context)
