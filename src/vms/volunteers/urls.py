from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from vms.volunteers.views import base

urlpatterns = [
    url(r'^$', base.HomeView.as_view(), name='home_page'),
    url(r'^volunteers/$', login_required(base.VolunteersView.as_view()), name='list'),
    url(r'^locations/$', login_required(base.LocationsView.as_view()), name='locations'),
    url(r'^schedule-list/$', login_required(base.ScheduleView.as_view()), name='schedule'),
    url(r'^schedule$', base.ScheduleApiView.as_view(), name='schedule_api'),
    url(r'^schedule-test$', base.MockSchedule.as_view(), name='schedule_mock'),
]
