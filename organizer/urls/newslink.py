from django.conf.urls import url

from ..views import (NewsLinkCreateView, NewsLinkDeleteView,

                     NewsLinkUpdateView)


urlpatterns = [
    url(r'^create/$', NewsLinkCreateView.as_view(),
        name='organizer_newslink_create'),
    url(r'^update/(?P<pk>\d+)/$', NewsLinkUpdateView.as_view(),
        name='organizer_newslink_update'),
    url(r'^delete/(?P<pk>\d)/$', NewsLinkDeleteView.as_view(),
        name='organizer_newslink_delete'),
]
