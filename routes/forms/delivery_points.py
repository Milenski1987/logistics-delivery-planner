from django import forms
import common.mixins
from routes.models import DeliveryPoint


class BaseDeliveryPointsFrom(forms.ModelForm):
    class Meta:
        model = DeliveryPoint
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter name for this Delivery Point...'
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Delivery Point address...'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Delivery Point city...'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'You can add Delivery Point information here...'
                }
            )
        }

        help_texts = {
            'description': 'This field is optional'
        }

        error_messages = {
            'name': {
                'unique': 'Delivery Point with this name already exist!',
                'required': 'Please enter a name!'
            },
            'address': {
                'required': 'Please enter an address!'
            },
            'city': {
                'required': 'Please enter a city!'
            }
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.name = instance.name.capitalize()
        instance.city = instance.city.capitalize()


        if commit:
            instance.save()
            self.save_m2m()

        return instance


class DeliveryPointDeleteForm(common.mixins.ReadOnlyFieldsMixin, BaseDeliveryPointsFrom):
    ...

class DeliveryPointAddForm(BaseDeliveryPointsFrom):
    ...

class DeliveryPointEditForm(BaseDeliveryPointsFrom):
    ...