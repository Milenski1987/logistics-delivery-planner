from django import forms
from common.forms import SearchForm


class DriverSearchAndSortForm(SearchForm):
    sort = forms.ChoiceField(
        required=False,
        choices=[
            ('full_name', 'Name (A-Z)'),
            ('-full_name', 'Name (Z-A)'),
            ('years_of_experience', 'Experience (Low-High)'),
            ('-years_of_experience', 'Experience (High-Low)'),
        ],
        widget=forms.Select(
            {'class': 'form-select rounded-4'}
        )
    )