from datetime import timedelta

from django.contrib.auth.views import LoginView, LogoutView
from django.utils.timezone import now
from django.views.generic import ListView, TemplateView

from vms.entities.models import Volunteer, VolunteerSchedule, Location


class HomeView(TemplateView):
    template_name = 'home.html'


class VolunteersView(ListView):
    model = Volunteer
    template_name = 'volunteers.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('name')


class LocationsView(ListView):
    model = Location
    template_name = 'locations.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('id')


class ScheduleView(ListView):
    model = VolunteerSchedule
    template_name = 'schedule.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('projection__date')


class ScheduleApiView(ListView):
    model = VolunteerSchedule
    template_name = 'schedule_api'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.current().order_by('projection__date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.get_queryset()

        context['schedule'] = [proj for proj in qs if now() <= proj.projection.date + timedelta(
            minutes=proj.projection.movie.duration)]
        return context


class MockSchedule(TemplateView):
    template_name = 'schedule_mock.html'


class VMSLogin(LoginView):
    template_name = 'login.html'


class VMSLogout(LogoutView):
    template_name = 'logout.html'
