from typing import Any, Dict
from django.db.models import Q, QuerySet
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView, DeleteView
from common.forms import SearchForm
from common.mixins import ModifyFormData
from routes.forms.routes import RouteDeleteForm, RouteAddForm, RouteEditForm
from routes.mixins import RouteContextMixin
from routes.models import Route


class RouteListView(RouteContextMixin, ModifyFormData, ListView, FormView):
    model = Route
    template_name = 'routes/routes-list-page.html'
    context_object_name = 'routes'
    form_class = SearchForm
    paginate_by = 12


    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        search_by = self.request.GET.get('search', '')

        if search_by:
            queryset = queryset.filter(
                Q(name__icontains=search_by)
                |
                Q(start_location__icontains=search_by)
                |
                Q(end_location__icontains=search_by)
            )

        return queryset


class RouteDetailsView(RouteContextMixin, DetailView):
    model = Route
    template_name = 'routes/route-details-page.html'


class RouteCreateView(RouteContextMixin, CreateView):
    model = Route
    template_name = 'shared/base-add-page.html'
    form_class = RouteAddForm

    def get_success_url(self) -> str:
        return reverse('routes:route_details', kwargs={'pk': self.object.pk})


class RouteUpdateView(RouteContextMixin, UpdateView):
    model = Route
    template_name = 'shared/base-edit-page.html'
    form_class = RouteEditForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['back_url'] = 'routes:route_details'
        context['id'] = self.get_object().pk

        return context

    def get_success_url(self) -> str:
        return reverse('routes:route_details', kwargs={'pk': self.object.pk})


class RouteDeleteView(RouteContextMixin, DeleteView):
    model = Route
    template_name = 'shared/base-delete-page.html'
    success_url = reverse_lazy('routes:routes_list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['back_url'] = 'routes:route_details'
        context['id'] = self.get_object().pk
        context['form'] = RouteDeleteForm(instance=self.object)

        return context