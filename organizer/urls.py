"""organizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import (NewsLinkCreateView, NewsLinkUpdateView, NewsLinkDeleteView,
                    TagCreateView, TagUpdateView, tag_detail, tag_list,
                    StartupCreateView, startup_list, startup_detail, StartupUpdateView,
                    )


urlpatterns = [
    url(r'^newslink/create/$', NewsLinkCreateView.as_view(), name='organizer_newslink_create'),
    url(r'^newslink/update/(?P<pk>\d+)/$', NewsLinkUpdateView.as_view(), name='organizer_newslink_update'),
    url(r'^newslink/delete/(?P<pk>\d)/$', NewsLinkDeleteView.as_view(), name='organizer_newslink_delete'),
    url(r'^startup/$', startup_list, name='organizer_startup_list'),
    url(r'^startup/create/$', StartupCreateView.as_view(), name='organizer_startup_create'),
    url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
    url(r'^startup/(?P<slug>[\w\-]+)/update/$', StartupUpdateView.as_view(), name='organizer_startup_update'),
    url(r'^tag/$', tag_list, name='organizer_tag_list'),
    url(r'^tag/create/$', TagCreateView.as_view(), name='organizer_tag_create'),
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    url(r'^tag/(?P<slug>[\w\-]+)/update/$', TagUpdateView.as_view(), name='organizer_tag_update'),
]
