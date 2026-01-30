from django import forms

import common.mixins
from routes.models import DeliveryPoint

class BaseDeliveryPointsFrom(forms.ModelForm):
    class Meta:
        model = DeliveryPoint
        fields = '__all__'


class DeliveryPointDeleteForm(common.mixins.ReadOnlyFieldsMixin, BaseDeliveryPointsFrom):
    ...

class DeliveryPointAddForm(BaseDeliveryPointsFrom):
    ...

class DeliveryPointEditForm(BaseDeliveryPointsFrom):
    ...
