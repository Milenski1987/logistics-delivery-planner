from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from routes.forms.routes import RouteDeleteForm, RouteAddForm, RouteEditForm
from routes.forms.routes import RouteDeleteForm
from routes.models import Route


def route_add(request: HttpRequest) -> HttpResponse:
    form = RouteAddForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            route = form.save()

            return redirect('routes:route_details', pk=route.id)

    context = {
        'form': form
    }

    return render(request, 'routes/route-add-page.html', context)

def routes_list(request: HttpRequest) -> HttpResponse:
    routes = Route.objects.all()

    context = {
        'routes': routes
    }

    return render(request, 'routes/routes-list-page.html', context)

def route_detail(request: HttpRequest, pk: int) -> HttpResponse:
    route = get_object_or_404(Route, pk=pk)

    context = {
        'route': route
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
        'route': route
    }

    return render(request, 'routes/route-edit-page.html', context)

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
        'form': form
    }

    return render(request, 'routes/route-delete-page.html', context)
