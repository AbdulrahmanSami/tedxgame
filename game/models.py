# -*- coding: utf-8  -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField(default='question text', verbose_name='نص السؤال')
    def __str__(self):
        return self.question_text
class Choice (models.Model):
    question = models.ForeignKey(Question, related_name='choices',on_delete=models.CASCADE)
    choice_text = models.CharField(default='خيار', max_length=30)
    def __str__(self):
        return self.choice_text

