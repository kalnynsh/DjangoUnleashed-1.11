from django.conf.urls import url

from ..views import (TagCreateView, TagUpdateView,
                     TagDetailView, TagListView, TagDeleteView)


urlpatterns = [
    url(r'^$', TagListView.as_view(), name='organizer_tag_list'),
    url(r'^create/$', TagCreateView.as_view(),
        name='organizer_tag_create'),
    url(r'^(?P<slug>[\w\-]+)/$', TagDetailView.as_view(),
        name='organizer_tag_detail'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', TagDeleteView.as_view(),
        name='organizer_tag_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', TagUpdateView.as_view(),
        name='organizer_tag_update'),
]
