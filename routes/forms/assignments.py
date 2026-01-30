from django import forms

import common.mixins
from routes.models import Assignment

class BaseAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['created_at']

class AssignmentDeleteForm(common.mixins.ReadOnlyFieldsMixin, BaseAssignmentForm):
    ...

class AssignmentAddForm(BaseAssignmentForm):
    ...

class AssignmentEditForm(BaseAssignmentForm):
    ...