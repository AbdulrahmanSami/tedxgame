from django.contrib import admin
from game.models import Question,Choice, Game
# -*- coding: utf-8  -*-
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title','question_text']
admin.site.register(Question,QuestionAdmin)
class ChoiceAdmin(admin.ModelAdmin):
    fields = ['title','choice_text','question','next_question','icon']
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Game)