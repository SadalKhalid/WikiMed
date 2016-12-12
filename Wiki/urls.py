# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .forms import WikiSignupForm
from userena import views as userena_views
from userena import settings as userena_settings
import django.contrib.auth.views
from django.core.urlresolvers import reverse
from .views import HomeListView, ArticleDetailView, ArticleCreateView, \
                   ArticleDeleteView, ArticleUpdateView, HomePageView,ProjectPageView ,\
                   translating_page_view, Article_page, Mark_Article_As_Finish


urlpatterns = [

    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^Medproject/$', ProjectPageView, name='project-page'),
    url(r'^translation/$', translating_page_view.as_view(), name='translating-page'),
    url(r'^Articles', HomeListView.as_view(), name="Wiki-home"),
    url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name="article-detail"),
    url(r'^(?P<pk>\d+)/Article/$', Article_page.as_view(), name="article-page"),
    url(r'^(?P<pk>\d+)/Article/FinishedArticles$', Mark_Article_As_Finish.as_view(),name="finished-article"),
    url(r'^create/$', ArticleCreateView.as_view(), name="article-create"),
    url(r'^delete/(?P<pk>\d+)/$', ArticleDeleteView.as_view(), name="article-delete"),
    url(r'^update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name="article-update"),
   # url(r'^accounts/signup/$', 'userena.views.signup', {'signup_form': WikiSignupForm, 'template_name': 'Wiki/signup_form.html'}),
   # url(r'^accounts/', include('userena.urls')),
  #  url(r'^accounts/resend/$', 'accounts.views.resend_confirmation_key', name='resend_confirmation_key'),
   # url(r'^accounts/signin/$', 'userena.views.signin', {'auth_form': ModifiedAuthenticationForm}),
  #  url(r'^accounts/edit/$', 'accounts.views.edit_common_profile', name='edit_common_profile'),
]
