# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    ar_first_name = models.CharField(max_length=30,
                                     verbose_name=u'الاسم الأول')
    ar_middle_name = models.CharField(max_length=30,
                                      verbose_name=u'الاسم الأوسط')
    ar_last_name = models.CharField(max_length=30,
                                    verbose_name=u'الاسم الأخير')
    mobile_number = models.CharField(max_length=20,
                                     verbose_name=u'رقم الجوال')
    picture = models.ImageField(upload_to=None,blank=True, null=True)

    def __unicode__(self):
        return self.ar_first_name


class Article(models.Model):
    translator = models.ForeignKey(User, related_name='translator_name',blank=True)
    en_name = models.CharField(max_length=100,
                               verbose_name=u'عنوان المقالة باللغة الانجليزية')
    ar_name = models.CharField(max_length=100, blank=True,
                               verbose_name=u'عنوان المقالة باللغة العربية')
    addition_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name=u'تاريخ الإضافة')
    en_link = models.URLField(max_length=200,
                              verbose_name=u'رابط المقالة باللغة الانجليزية')
    ar_link = models.URLField(max_length=200, blank=True,
                              verbose_name=u'رابط المقالة باللغة العربية')
    when_accredit = models.DateTimeField(null=True, blank=True,
                                         verbose_name=u'متى اعتمدت؟ ')
    is_it_accredit = models.NullBooleanField(verbose_name=u'هل هي معتمدة؟ ')
    is_it_translated = models.NullBooleanField(verbose_name=u'هل تُرجمت؟')
    when_translated = models.DateTimeField( null=True, blank=True,
                                            verbose_name=u'متى تُرجمت؟')

    def __unicode__(self):
        return self.en_name

class Activity(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    description=models.TextField(max_length=200)
    place=models.CharField(max_length=100)
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
