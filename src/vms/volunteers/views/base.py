from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

from vms.entities.models import Volunteer, VolunteerSchedule


def index(request):
    return HttpResponse("Hello, world. TIFF Volunteer Management System.")


class VolunteersView(ListView):
    model = Volunteer
    template_name = 'volunteers.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('name')


class ScheduleView(ListView):
    model = VolunteerSchedule
    template_name = 'schedule.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('projection__date')


class MockSchedule(TemplateView):
    template_name = 'schedule.html'
