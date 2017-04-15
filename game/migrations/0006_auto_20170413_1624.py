# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-13 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20170413_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Question')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='flag',
            field=models.CharField(blank=True, default='choice title', max_length=30),
        ),
        migrations.AddField(
            model_name='choice',
            name='icon',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='choice',
            name='next_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leading_choices', to='game.Question'),
        ),
    ]
