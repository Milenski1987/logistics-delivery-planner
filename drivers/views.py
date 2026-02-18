from django.db.models import QuerySet
from django.views.generic import ListView, FormView, DetailView
from common.mixins import ModifyFormData
from drivers.forms import DriverSearchAndSortForm
from drivers.mixins import DriverContextMixin
from drivers.models import Driver


class DriverListView(DriverContextMixin,ModifyFormData ,ListView, FormView):
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