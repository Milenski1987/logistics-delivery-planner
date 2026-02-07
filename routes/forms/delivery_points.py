from django import forms

import common.mixins
from routes.models import DeliveryPoint

class BaseDeliveryPointsFrom(forms.ModelForm):
    class Meta:
        model = DeliveryPoint
        fields = '__all__'

        error_messages = {
            'name': {
                'unique': 'Delivery Point with this name already exist'
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class DeliveryPointDeleteForm(common.mixins.ReadOnlyFieldsMixin, BaseDeliveryPointsFrom):
    ...

class DeliveryPointAddForm(BaseDeliveryPointsFrom):
    ...

class DeliveryPointEditForm(BaseDeliveryPointsFrom):
    ...
