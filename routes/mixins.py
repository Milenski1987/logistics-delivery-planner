from typing import Dict, Any
from django.db import models


class TimeStampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False
    )


class RouteContextMixin:
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Route'
        context['icon'] = 'images/route_icon.png'
        context['back_url'] = 'routes:routes_list'

        return context


class DeliveryPointContextMixin:
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delivery Point'
        context['icon'] = 'images/delivery_point_icon.png'
        context['back_url'] = 'routes:delivery_points_list'

        return context


class AssignmentContextMixin:
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Assignment'
        context['icon'] = 'images/assignment_icon.png'
        context['back_url'] = 'routes:assignment_list'

        return context