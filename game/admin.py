from django.contrib import admin
from game.models import Question,Choice
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text']
admin.site.register(Question,QuestionAdmin)
class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text','question']
admin.site.register(Choice,ChoiceAdmin)