from django.conf.urls import url

from ..views import (StartupCreateView, StartupDeleteView,
                     StartupUpdateView, startup_detail, StartupListView)

urlpatterns = [
    url(r'^$', StartupListView.as_view(),
        name='organizer_startup_list'),
    url(r'^create/$', StartupCreateView.as_view(),
        name='organizer_startup_create'),
    url(r'^(?P<slug>[\w\-]+)/$', startup_detail,
        name='organizer_startup_detail'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', StartupDeleteView.as_view(),
        name='organizer_startup_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', StartupUpdateView.as_view(),
        name='organizer_startup_update'),
]
