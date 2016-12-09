# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.core.urlresolvers import reverse
from .views import HomeListView, ArticleDetailView, ArticleCreateView, \
                   ArticleDeleteView, ArticleUpdateView, HomePageView,ProjectPageView ,\
                   translating_page_view


urlpatterns = [

    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^Medproject/$', ProjectPageView, name='project-page'),
    url(r'^translation/$', translating_page_view.as_view(), name='translating-page'),
    url(r'^Articles', HomeListView.as_view(), name="Wiki-home"),
   # url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name="article-detail"),
    url(r'^create/$', ArticleCreateView.as_view(), name="article-create"),
    url(r'^delete/(?P<pk>\d+)/$', ArticleDeleteView.as_view(), name="article-delete"),
    url(r'^update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name="article-update"),
]
