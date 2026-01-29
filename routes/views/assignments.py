from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from routes.forms.assignments import AssignmentDeleteForm, AssignmentAddForm, AssignmentEditForm
from routes.models import Assignment


def assignment_add(request: HttpRequest) -> HttpResponse:
    form = AssignmentAddForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            assignment = form.save()

            return redirect('routes:assignment_details', pk=assignment.id)

    context = {
        'form': form
    }
    return render(request, 'routes/assignment-add-page.html', context)

def assignment_list(request: HttpRequest) -> HttpResponse:
    assignments = Assignment.objects.all()

    context = {
        'assignments': assignments
    }

    return render(request, 'routes/assignments-list-page.html', context)

def assignment_detail(request: HttpRequest, pk: int) -> HttpResponse:
    assignment = get_object_or_404(Assignment, pk=pk)

    context = {
        'assignment': assignment
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
        'assignment': assignment
    }

    return render(request, 'routes/assignment-edit-page.html', context)

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
        'form': form
    }

    return render(request, 'routes/assignment-delete-page.html', context)