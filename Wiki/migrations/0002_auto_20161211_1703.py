# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='addition_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0625\u0636\u0627\u0641\u0629'),
        ),
        migrations.AlterField(
            model_name='article',
            name='ar_link',
            field=models.URLField(blank=True, verbose_name='\u0631\u0627\u0628\u0637 \u0627\u0644\u0645\u0642\u0627\u0644\u0629 \u0628\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629'),
        ),
        migrations.AlterField(
            model_name='article',
            name='ar_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u0639\u0646\u0648\u0627\u0646 \u0627\u0644\u0645\u0642\u0627\u0644\u0629 \u0628\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629'),
        ),
        migrations.AlterField(
            model_name='article',
            name='en_link',
            field=models.URLField(verbose_name='\u0631\u0627\u0628\u0637 \u0627\u0644\u0645\u0642\u0627\u0644\u0629 \u0628\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629'),
        ),
        migrations.AlterField(
            model_name='article',
            name='en_name',
            field=models.CharField(max_length=100, verbose_name='\u0639\u0646\u0648\u0627\u0646 \u0627\u0644\u0645\u0642\u0627\u0644\u0629 \u0628\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_it_accredit',
            field=models.NullBooleanField(verbose_name='\u0647\u0644 \u0647\u064a \u0645\u0639\u062a\u0645\u062f\u0629\u061f '),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_it_translated',
            field=models.NullBooleanField(verbose_name='\u0647\u0644 \u062a\u064f\u0631\u062c\u0645\u062a\u061f'),
        ),
        migrations.AlterField(
            model_name='article',
            name='when_accredit',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u0645\u062a\u0649 \u0627\u0639\u062a\u0645\u062f\u062a\u061f '),
        ),
        migrations.AlterField(
            model_name='article',
            name='when_translated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u0645\u062a\u0649 \u062a\u064f\u0631\u062c\u0645\u062a\u061f'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
