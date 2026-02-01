from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

import common.mixins
from routes.models import Assignment

class BaseAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['created_at']
        widgets = {
            'assignment_start':forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_assignment_start(self):
        start_date = self.cleaned_data.get('assignment_start')

        if start_date < datetime.now().date():
            raise ValidationError('Past dates are not allowed')
        return start_date

class AssignmentDeleteForm(common.mixins.ReadOnlyFieldsMixin, BaseAssignmentForm):
    ...

class AssignmentAddForm(BaseAssignmentForm):
    ...

class AssignmentEditForm(BaseAssignmentForm):
    ...