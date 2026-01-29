from django import forms

import common.mixins
from routes.models import Route


class RouteDeleteForm(forms.ModelForm, common.mixins.DisableFormFieldsMixin):
    ...

class RouteAddForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'points_for_delivery':forms.CheckboxSelectMultiple()
        }
        help_texts={
            'points_for_delivery': 'Can choose more 1 or more'
        }

class RouteEditForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'points_for_delivery':forms.CheckboxSelectMultiple()
        }
        help_texts={
            'points_for_delivery': 'Can choose more 1 or more'
        }