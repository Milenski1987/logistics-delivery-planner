from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from common.forms import SearchForm
from routes.forms.assignments import AssignmentDeleteForm, AssignmentAddForm, AssignmentEditForm
from routes.models import Assignment


def assignment_add(request: HttpRequest) -> HttpResponse:
    form = AssignmentAddForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            assignment = form.save()

            return redirect('routes:assignment_details', pk=assignment.id)

    context = {
        'form': form,
        'title': 'Assignment',
        'back_url': 'routes:assignment_list',
        'icon': 'images/assignment_icon.png'
    }
    return render(request, 'shared/base-add-page.html', context)

def assignment_list(request: HttpRequest) -> HttpResponse:
    assignments = Assignment.objects.all().order_by('assignment_start')
    form = SearchForm(request.GET or None)

    if request.method == 'GET':
        if form.is_valid():
            search_by = form.cleaned_data['search']
            assignments = Assignment.objects.filter(
                Q(route__name__icontains=search_by)
                |
                Q(route__points_for_delivery__name__icontains=search_by)
                |
                Q(driver__full_name__icontains=search_by)
                |
                Q(vehicle__make__icontains=search_by)
            ).order_by('assignment_start')

    context = {
        'assignments': assignments,
        'form': form,
        'title': 'assignment'
    }

    return render(request, 'routes/assignments-list-page.html', context)

def assignment_detail(request: HttpRequest, pk: int) -> HttpResponse:
    assignment = get_object_or_404(Assignment, pk=pk)

    context = {
        'assignment': assignment,
        'title': 'Assignment',
        'icon': 'images/assignment_icon.png'
    }
    return render(request, 'routes/assignment-details-page.html', context)

def assignment_edit(request: HttpRequest, pk: int) -> HttpResponse:
    assignment = get_object_or_404(Assignment, pk=pk)
    form = AssignmentEditForm(
        request.POST or None,
        instance=assignment
    )

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('routes:assignment_details', pk=pk)

    context = {
        'form': form,
        'title': 'Assignment',
        'id': assignment.id,
        'back_url': 'routes:assignment_details',
        'icon': 'images/assignment_icon.png'
    }

    return render(request, 'shared/base-edit-page.html', context)

def assignment_delete(request: HttpRequest, pk: int) -> HttpResponse:
    assignment = get_object_or_404(Assignment, pk=pk)
    form = AssignmentDeleteForm(
        request.POST or None,
        instance=assignment
    )

    if request.method == "POST":
        if form.is_valid():
            assignment.delete()

            return redirect('routes:assignment_list')

    context = {
        'form': form,
        'title': 'Assignment',
        'id': assignment.id,
        'back_url': 'routes:assignment_details',
        'icon': 'images/assignment_icon.png'
    }

    return render(request, 'shared/base-delete-page.html', context)