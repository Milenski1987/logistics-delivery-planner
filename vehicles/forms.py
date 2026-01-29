from django import forms


class VehicleSearchAndSortForm(forms.Form):
    search = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.SearchInput(
            {'placeholder': 'Search:'}
        ),
        label='Search by make:'
    )

    sort = forms.ChoiceField(
        required=False,
        choices=[
            ('make', 'Make (A-Z)'),
            ('-make', 'Make (Z-A)'),
            ('capacity_kg', 'Capacity in kg (Low-High)'),
            ('-capacity_kg', 'Capacity in kg (High-Low)'),
        ],
        label='Sort Vehicle by:'
    )