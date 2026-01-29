from django import forms

import common.mixins
from routes.models import DeliveryPoint


class DeliveryPointDeleteForm(forms.ModelForm, common.mixins.DisableFormFieldsMixin):
    ...


class DeliveryPointAddForm(forms.ModelForm):
    class Meta:
        model = DeliveryPoint
        fields = '__all__'

class DeliveryPointEditForm(forms.ModelForm):
    class Meta:
        model = DeliveryPoint
        fields = '__all__'
