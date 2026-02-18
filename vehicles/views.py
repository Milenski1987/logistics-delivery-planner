from django.db.models import QuerySet
from django.views.generic import ListView, FormView, DetailView
from common.mixins import ModifyFormData
from vehicles.forms import VehicleSearchAndSortForm
from vehicles.mixins import VehicleContextMixin
from vehicles.models import Vehicle


class VehicleListView(VehicleContextMixin,ModifyFormData ,ListView, FormView):
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