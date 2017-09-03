from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from vms.volunteers import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home_page'),
    url(r'^volunteers/$',
        login_required(views.VolunteersView.as_view()), name='list'),
    url(r'^locations/$',
        login_required(views.LocationsView.as_view()), name='locations'),
    url(r'^schedule/list/$',
        login_required(views.ScheduleView.as_view()), name='schedule'),
    url(r'^schedule$', views.ScheduleApiView.as_view(), name='schedule_api'),
    url(r'^schedule-test$', views.MockSchedule.as_view(), name='schedule_mock'),
]
