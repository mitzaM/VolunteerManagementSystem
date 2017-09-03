from django.forms import ModelForm

from vms.entities.models import VolunteerSchedule


class AddScheduleForm(ModelForm):
    class Meta:
        model = VolunteerSchedule
        fields = [
            'projection',
            'volunteer_1',
            'volunteer_2',
        ]


class EditScheduleForm(ModelForm):
    class Meta:
        model = VolunteerSchedule
        fields = [
            'projection',
            'volunteer_1',
            'volunteer_2',
        ]
