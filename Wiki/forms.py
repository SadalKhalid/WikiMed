from django.forms import ModelForm

from .models import Article


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['translator','en_name','en_link']