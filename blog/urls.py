from django.conf.urls import url

from .views import PostArchiveMonthView, PostArchiveYearView, PostCreateView, \
                    PostDeleteView, PostDetailView,  PostListView, PostUpdateView


urlpatterns = [
    url(r'^$', PostListView.as_view(), {'parent_template': 'base.html'}, name='blog_post_list'),
    url(r'^create/$', PostCreateView.as_view(), name='blog_post_create'),
    url(r'^(?P<year>\d{4})/$', PostArchiveYearView.as_view(), name='blog_post_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', PostArchiveMonthView.as_view(), name='blog_post_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[\w\-]+)/$',
        PostDetailView.as_view(), name='blog_post_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/delete/$',
        PostDeleteView.as_view(),
        name='blog_post_delete'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/update/$',
        PostUpdateView.as_view(), name='blog_post_update'),
]
