from django import forms

import common.mixins
from routes.models import Assignment


class AssignmentDeleteForm(forms.ModelForm, common.mixins.DisableFormFieldsMixin):
    ...

class AssignmentAddForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['created_at']

class AssignmentEditForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['created_at']