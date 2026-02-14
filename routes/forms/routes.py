from typing import Optional
from django import forms
from django.core.exceptions import ValidationError
import common.mixins
from routes.models import Route


class BaseRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Route name...'
                }
            ),
            'start_location': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Route start location...'
                }
            ),
            'end_location': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Route end location...'
                }
            ),
            'distance_km': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Route distance...'
                }
            ),
            'points_for_delivery':forms.CheckboxSelectMultiple()
        }

        help_texts={
            'points_for_delivery': 'You can choose multiple points for delivery'
        }

        labels = {
            'distance_km': 'Distance in km'
        }

        error_messages = {
            'name':{
                'required': 'Please enter Route name!'
            },
            'start_location': {
                'required': 'Please enter Route start location!'
            },
            'end_location':{
                'required': 'Please enter Route end location'
            },
            'distance_km':{
                'required': 'Please enter Route distance',
                'invalid': 'Please enter valid distance in KM'
            }
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.label != 'Points for delivery':
                field.widget.attrs.update({'class': 'form-control'})

    def clean_start_location(self) -> Optional[str]:
        location = self.cleaned_data.get('start_location')
        if not location.isalpha():
            raise ValidationError('Start location must contain only letters.')
        return location

    def clean_end_location(self) -> Optional[str]:
        location = self.cleaned_data.get('end_location')
        if not location.isalpha():
            raise ValidationError('End location must contain only letters.')
        return location


class RouteDeleteForm(common.mixins.ReadOnlyFieldsMixin, BaseRouteForm):
    class Meta(BaseRouteForm.Meta):
        widgets = {}
        help_texts = {}


class RouteAddForm(BaseRouteForm):
    ...


class RouteEditForm(BaseRouteForm):
    ...
