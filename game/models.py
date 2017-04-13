# -*- coding: utf-8  -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Game(models.Model):
    first_question = models.ForeignKey('Question', on_delete=models.CASCADE)

class Question(models.Model):
    question_text = models.TextField(default="question text", verbose_name='نص السؤال')
    title = models.CharField(default='question title', max_length=30)
    def __str__(self):
        return self.title
class Choice (models.Model):
    question = models.ForeignKey(Question, related_name='choices',on_delete=models.CASCADE)
    next_question = models.ForeignKey(Question, related_name="leading_choices", on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(default='خيار', max_length=30)
    title = models.CharField(default='choice title', max_length=30)
    icon = models.CharField(max_length=30, blank=True)
    flag = models.CharField(default='choice title', max_length=30, blank=True)
    def __str__(self):
        return self.title

