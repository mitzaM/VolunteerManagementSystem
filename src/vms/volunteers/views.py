from django.contrib.auth.views import LoginView, LogoutView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from vms.entities.models import Volunteer, VolunteerSchedule, Location
from vms.volunteers.forms import AddScheduleForm, EditScheduleForm


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


class ScheduleAddView(CreateView):
    model = VolunteerSchedule
    form_class = AddScheduleForm
    template_name = 'schedule_add.html'
    success_url = reverse_lazy('volunteers:schedule')


class ScheduleEditView(UpdateView):
    model = VolunteerSchedule
    form_class = EditScheduleForm
    template_name = 'schedule_edit.html'
    success_url = reverse_lazy('volunteers:schedule')


class ScheduleDeleteView(DeleteView):
    model = VolunteerSchedule
    template_name = 'schedule_delete.html'
    success_url = reverse_lazy('volunteers:schedule')


class ScheduleApiView(ListView):
    model = VolunteerSchedule
    template_name = 'schedule_api'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.current().order_by('projection__date')


class MockSchedule(TemplateView):
    template_name = 'schedule_mock.html'


class VMSLogin(LoginView):
    template_name = 'login.html'


class VMSLogout(LogoutView):
    template_name = 'logout.html'
