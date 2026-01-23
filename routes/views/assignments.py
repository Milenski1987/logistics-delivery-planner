from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def assignment_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'routes/assignment-add-page.html')

def assignment_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'routes/assignments-list-page.html')

def assignment_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'routes/assignment-details-page.html')

def assignment_edit(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'routes/assignment-edit-page.html')

def assignment_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'routes/assignment-delete-page.html')