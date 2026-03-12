from typing import Any, Dict
from django.db.models import QuerySet
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView, DetailView, UpdateView, CreateView, DeleteView
from common.mixins import ModifyFormData
from vehicles.forms import VehicleSearchAndSortForm, VehicleEditForm, VehicleAddForm, VehicleDeleteForm
from vehicles.mixins import VehicleContextMixin
from vehicles.models import Vehicle


class VehicleListView(ModifyFormData ,ListView, FormView):
    model = Vehicle
    template_name = 'vehicle/vehicles-list.html'
    context_object_name = 'vehicles'
    form_class = VehicleSearchAndSortForm
    paginate_by = 15

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()

        search_by = self.request.GET.get('search', '')
        sort_by = self.request.GET.get('sort', '')

        if search_by:
            queryset = queryset.filter(make__icontains=search_by)

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset


class VehicleDetailView(VehicleContextMixin, DetailView):
    model = Vehicle
    template_name = 'vehicle/vehicle-details.html'


class VehicleCreateView(VehicleContextMixin, CreateView):
    model = Vehicle
    template_name = 'vehicle/vehicle-create.html'
    form_class = VehicleAddForm

    def get_success_url(self) -> str:
        return reverse('vehicle:details', kwargs={'pk': self.object.pk})


class VehicleUpdateView(VehicleContextMixin, UpdateView):
    model = Vehicle
    template_name = 'vehicle/vehicle-update.html'
    form_class = VehicleEditForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['back_url'] = 'vehicle:details'
        context['id'] = self.get_object().pk

        return context

    def get_success_url(self) -> str:
        return reverse('vehicle:details', kwargs={'pk': self.object.pk})


class VehicleDeleteView(VehicleContextMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle/vehicle-delete.html'
    success_url = reverse_lazy('vehicle:list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['back_url'] = 'vehicle:details'
        context['id'] = self.get_object().pk
        context['form'] = VehicleDeleteForm(instance=self.object)

        return context