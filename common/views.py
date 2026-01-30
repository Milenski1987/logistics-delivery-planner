from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.http import Http404

def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'common/home-page.html')

