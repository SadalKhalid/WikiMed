# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, RedirectView
from django.views.generic.base import TemplateView
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
# Create your views here.



class HomePageView(TemplateView):
    template_name = "Wiki/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

#class ProjectPageView(DetailView):
#    template_name = "Wiki/project_page.html"

#    def get_object(self,request):
#        return get_object_or_404(User, pk=request.user['user_id'])

def ProjectPageView (request):
    return render(request,"Wiki/project_page.html")

class translating_page_view(ListView):
    queryset = Article.objects.all()
    model = Article
    template_name ="Wiki/translating_page.html"



class Article_page(DetailView):
    template_name = "wiki/Article_page.html"
    model = Article
    #en_name
    #en_link
    #when_translated



class HomeListView(ListView):
    template_name = "Wiki/articles_home.html"
    model = Article


   # def superuser_only(function):
     #   def _inner(request, *args, **kwargs):
      #      if not request.user.is_superuser:
     #           raise PermissionDenied
        #    return function(request, *args, **kwargs)


class HomeRedirectView(RedirectView):
    url = reverse_lazy('Wiki-home')


class ArticleDetailView(DetailView):
    template_name = "Wiki/article.html"
    model = Article
    User == Article.translator
    if not User.is_superuser:
        raise PermissionDenied


class ArticleCreateView(CreateView):
    template_name = "Wiki/article_create.html"
    form_class = ArticleForm
    if not User.is_superuser:
        raise PermissionDenied

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDeleteView(DeleteView):
    success_url = reverse_lazy('translating-page')
    model = Article
   # if not User.is_superuser:
    #    raise PermissionDenied
  #  def delete(self, request, *args, **kwargs):
    #    self.object = self.get_object()
    #    success_url = self.get_success_url()
    #    self.object.delete()
    #    return HttpResponseRedirect(success_url)

    #success_url = reverse_lazy('article-delete'‌)
    #success_url = reverse_lazy('wiki/article.html')


class ArticleUpdateView(UpdateView):
    template_name = "Wiki/article_update.html"
    model = Article
    form_class = ArticleForm
    if not User.is_superuser:
        raise PermissionDenied