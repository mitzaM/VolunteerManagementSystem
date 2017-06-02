from datetime import timedelta

from django.http import HttpResponse
from django.utils.timezone import now
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
        return qs.current().order_by('projection__date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.get_queryset()

        proj = [p for p in qs if now() <= p.projection.date + timedelta(
            minutes=p.projection.movie.duration)]
        context['schedule'] = proj
        return context


class MockSchedule(TemplateView):
    template_name = 'schedule_mock.html'
