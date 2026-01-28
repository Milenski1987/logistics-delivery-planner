from django import forms


class DriverSearchAndSortForm(forms.Form):
    search = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.SearchInput(
            {'placeholder': 'Enter name'}
        ),
        label='Search Drivers by Name:'
    )

    sort = forms.ChoiceField(
        required=False,
        choices=[
            ('full_name', 'Name (A-Z)'),
            ('-full_name', 'Name (Z-A)'),
            ('years_of_experience', 'Experience (Low-High)'),
            ('-years_of_experience', 'Experience (High-Low)'),
        ],
        label='Sort Drivers by:'
    )