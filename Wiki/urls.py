from django.conf.urls import url
from .views import HomeListView, ArticleDetailView, ArticleCreateView, \
                   ArticleDeleteView, ArticleUpdateView


urlpatterns = [
    url(r'^$', HomeListView.as_view(), name="Wiki-home"),
    url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name="article-detail"),
    url(r'^create/$', ArticleCreateView.as_view(), name="article-create"),
    url(r'^delete/(?P<pk>\d+)/$', ArticleDeleteView.as_view(), name="article-delete"),
    url(r'^update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name="article-update"),
]
