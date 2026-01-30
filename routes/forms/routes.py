from django import forms

import common.mixins
from routes.models import Route

class BaseRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'points_for_delivery':forms.CheckboxSelectMultiple()
        }
        help_texts={
            'points_for_delivery': 'Can choose more 1 or more'
        }

class RouteDeleteForm(common.mixins.ReadOnlyFieldsMixin, BaseRouteForm):
    class Meta(BaseRouteForm.Meta):
        widgets = {}
        help_texts = {}

class RouteAddForm(BaseRouteForm):
    ...

class RouteEditForm(BaseRouteForm):
    ...