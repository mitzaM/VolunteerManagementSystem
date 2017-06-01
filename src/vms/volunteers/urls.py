from django.conf.urls import url

from vms.volunteers.views import base

urlpatterns = [
    url(r'^$', base.index, name='index'),
    url(r'^volunteers$', base.VolunteersView.as_view(), name='volunteers_list'),
    # url(r'^schedule$', base.ScheduleView.as_view(), name='schedule'),
    url(r'^schedule$', base.MockSchedule.as_view(), name='schedule'),
]
