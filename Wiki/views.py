from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, \
UpdateView, RedirectView
from .models import Article
from .forms import ArticleForm
# Create your views here.

class HomeListView(ListView):
    template_name = "Wiki/articles_home.html"
    model = Article


class HomeRedirectView(RedirectView):
    url = reverse_lazy('Wiki-home')


class ArticleDetailView(DetailView):
    template_name = "Wiki/article.html"
    model = Article


class ArticleCreateView(CreateView):
    template_name = "Wiki/article_create.html"
    form_class = ArticleForm

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog-home')


class ArticleUpdateView(UpdateView):
    template_name = "Wiki/article_update.html"
    model = Article
    form_class = ArticleForm