from django import forms


class SearchForm(forms.Form):

    search = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.SearchInput(
            {'placeholder': 'Search...',
             'class': 'form-control rounded-4'}
        ),
    )

