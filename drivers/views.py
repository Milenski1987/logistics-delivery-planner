from typing import Any, Dict
from django.db.models import QuerySet, ProtectedError
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView, DeleteView
from common.mixins import ModifyFormData
from drivers.forms import DriverSearchAndSortForm, DriverAddForm, DriverEditForm, DriverDeleteForm
from drivers.mixins import DriverContextMixin
from drivers.models import Driver


class DriverListView(ModifyFormData ,ListView, FormView):
    model = Driver
    template_name = 'driver/drivers-list.html'
    context_object_name = 'drivers'
    form_class = DriverSearchAndSortForm
    paginate_by = 15

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()

        search_by = self.request.GET.get('search', '')
        sort_by = self.request.GET.get('sort', '')

        if 'search' in self.request.GET:
            queryset = queryset.filter(full_name__icontains=search_by)

        if 'sort' in self.request.GET:
            queryset = queryset.order_by(sort_by)

        return queryset


class DriverDetailView(DriverContextMixin, DetailView):
    model = Driver
    template_name = 'driver/driver-details.html'


class DriverCreateView(DriverContextMixin, CreateView):
    model = Driver
    template_name = 'driver/driver-create.html'
    form_class = DriverAddForm

    def get_success_url(self) -> str:
        return reverse('driver:details', kwargs={'pk': self.object.pk})


class DriverUpdateView(DriverContextMixin, UpdateView):
    model = Driver
    template_name = 'driver/driver-update.html'
    form_class = DriverEditForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['back_url'] = 'driver:details'
        context['id'] = self.get_object().pk

        return context

    def get_success_url(self) -> str:
        return reverse('driver:details', kwargs={'pk': self.object.pk})


class DriverDeleteView(DriverContextMixin, DeleteView):
    model = Driver
    template_name = 'driver/driver-delete.html'
    success_url = reverse_lazy('driver:list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['back_url'] = 'driver:details'
        context['id'] = self.object.pk
        context['form'] = DriverDeleteForm(instance=self.object)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        try:
            return super().post(request, *args, **kwargs)

        except ProtectedError:
            messages.error(request,"Unable to delete: Driver has active assignments.")

            return redirect('driver:delete', pk=self.object.pk)