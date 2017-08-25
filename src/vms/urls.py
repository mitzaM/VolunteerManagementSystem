from django.conf.urls import url, include
from django.contrib import admin

from vms.volunteers.urls import urlpatterns as volunteer_urls
from vms.volunteers.views.base import VMSLogin, VMSLogout

urlpatterns = [
    url(r'^', include(volunteer_urls, namespace='volunteers')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', VMSLogin.as_view(), name='login'),
    url(r'^logout/$', VMSLogout.as_view(), name='logout'),
]
