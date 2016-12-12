#encoding:utf-8

from __future__ import unicode_literals
from django.forms import ModelForm
from .models import Article, Profile
from userena.utils import get_profile_model

from django.contrib.auth import get_user_model

from userena import settings as userena_settings
from django.utils.translation import gettext as _
from userena.models import UserenaSignup
from userena.forms import SignupForm

from django import forms



class WikiSignupForm(SignupForm):
    ar_first_name = forms.CharField(label=Profile._meta.get_field('ar_first_name').verbose_name,
                                    max_length=30)
    ar_middle_name = forms.CharField(label=Profile._meta.get_field('ar_middle_name').verbose_name,
                                     max_length=30)
    ar_last_name = forms.CharField(label=Profile._meta.get_field('ar_last_name').verbose_name,
                                   max_length=30)
    mobile_number = forms.CharField(label=Profile._meta.get_field('mobile_number').verbose_name,
                                   max_length=30)


    def __init__(self, *args, **kw):
        super(WikiSignupForm, self).__init__(*args, **kw)
        del self.fields['username']

    def clean(self):
        # Call the parent class's clean function.
        cleaned_data = super(WikiSignupForm, self).clean()

        # Remove spaces at the start and end of all text fields.
        for field in cleaned_data:
            if isinstance(cleaned_data[field], unicode):
                cleaned_data[field] = cleaned_data[field].strip()


        if 'mobile_number' in cleaned_data:
            mobile_number_msg = ""
            cleaned_data['mobile_number'] = core.utils.hindi_to_arabic(cleaned_data['mobile_number'])
            if len(cleaned_data['mobile_number']) < 10:
                mobile_number_msg = u"الرقم الذي أدخلت ناقص"
            if not all([number in '1234567890+' for number in cleaned_data['mobile_number']]):
                mobile_number_msg = u"أدخل أرقاما فقط"
            if mobile_number_msg:
                self._errors['mobile_number'] = self.error_class([mobile_number_msg])
                del cleaned_data['mobile_number']

        return cleaned_data

    def save(self):
        self.cleaned_data['email'] = self.cleaned_data['email'].lower()
        self.cleaned_data['username'] = self.cleaned_data['email'].split('@')[0]
        self.cleaned_data['username'] = self.cleaned_data['username']
        new_user = super(WikiSignupForm, self).save()
        return new_user


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['translator','en_name','en_link']