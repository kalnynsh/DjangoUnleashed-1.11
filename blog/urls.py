from django.conf.urls import url

from .views import PostCreateView, post_detail, PostListView, PostUpdateView


urlpatterns = [
    url(r'^$', PostListView.as_view(), {'parent_template': 'base.html'}, name='blog_post_list'),
    url(r'^create/$', PostCreateView.as_view(), name='blog_post_create'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$',
        post_detail,
        {'parent_template': 'base.html'},
        name='blog_post_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$',
        PostUpdateView.as_view(), name='blog_post_update'),
]
