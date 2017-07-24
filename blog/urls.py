from django.conf.urls import url

from .views import post_detail, PostListView


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog_post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$',
        post_detail, name='blog_post_detail'),
]
