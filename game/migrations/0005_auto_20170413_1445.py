# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-13 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_question_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='title',
            field=models.CharField(default='choice title', max_length=30),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default='question title', max_length=30),
        ),
    ]