from datetime import datetime, date
from typing import Optional
from django import forms
from django.core.exceptions import ValidationError
import common.mixins
from routes.models import Assignment


class BaseAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['created_at', 'updated_at']
        widgets = {
            'assignment_start':forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
            'notes': forms.Textarea(
                attrs={
                    'placeholder': 'Enter additional assignment information here'
                }
            )
        }

        help_texts = {
            'notes': 'This field is optional'
        }

        error_messages = {
            'route':{
                'required': 'Please choose a route!',
                'invalid': 'Please choose a route'
            },
            'driver':{
                'required': 'Please choose a driver!',
                'invalid': 'Please choose a driver'
            },
            'vehicle':{
                'required': 'Please choose a vehicle!',
                'invalid': 'Please choose a vehicle'
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_assignment_start(self) -> Optional[date]:
        start_date = self.cleaned_data.get('assignment_start')

        if start_date < datetime.now().date():
            raise ValidationError('Past dates are not allowed')
        return start_date

    def clean(self):
        cleaned = super().clean()
        assignment_start = cleaned.get('assignment_start')
        driver = cleaned.get('driver')
        vehicle = cleaned.get('vehicle')
        assignment_id = self.instance.pk or None

        available_assignments = (Assignment.objects.filter(assignment_start=assignment_start)
                                 .exclude(id=assignment_id)
                                 .select_related('driver', 'vehicle'))


        for assignment in available_assignments:
            if assignment.driver == driver:
                self.add_error('driver', f'Driver {assignment.driver.full_name} is not available for this date')

            if assignment.vehicle == vehicle:
                self.add_error('vehicle',f'Vehicle {assignment.vehicle} '
                                      f'with registration number {assignment.vehicle.registration_number} '
                                      f'is not available for this date')

        return cleaned


class AssignmentDeleteForm(common.mixins.ReadOnlyFieldsMixin, BaseAssignmentForm):
    ...


class AssignmentAddForm(BaseAssignmentForm):
    ...


class AssignmentEditForm(BaseAssignmentForm):
    ...
