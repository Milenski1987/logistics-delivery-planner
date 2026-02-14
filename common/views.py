from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'common/home-page.html'