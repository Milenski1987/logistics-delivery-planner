from django import forms
from common.forms import SearchForm


class VehicleSearchAndSortForm(SearchForm):

    sort = forms.ChoiceField(
        required=False,
        choices=[
            ('make', 'Make (A-Z)'),
            ('-make', 'Make (Z-A)'),
            ('capacity_kg', 'Capacity in kg (Low-High)'),
            ('-capacity_kg', 'Capacity in kg (High-Low)'),
        ],
        widget=forms.Select(
            {'class': 'form-select rounded-4'}
        )
    )