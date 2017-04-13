from django.shortcuts import render
from django.views.decorators import csrf
from .models import Choice, Question
from django.http import HttpResponse
import json
# -*- coding: utf-8  -*-
def handle_index(request):
    first_question = Question.objects.filter(leading_choices__isnull=True).first()
    return render(request, "game/index.html", {'first_question': first_question})

@csrf.csrf_exempt
def handle_ajax(request):
    choice_pk = request.POST['choice_pk']
    choice = Choice.objects.get(pk=choice_pk)
    if choice.next_question.choices.exists():
        response= {"next_question_text": choice.next_question.question_text,
                   "choice1_text": choice.next_question.choices.first().choice_text,
                   "choice1_pk": choice.next_question.choices.first().pk,
                   "choice1_icon": choice.next_question.choices.first().icon,
                   "choice2_icon": choice.next_question.choices.last().icon,
                   "choice2_text": choice.next_question.choices.last().choice_text,
                   "choice2_pk": choice.next_question.choices.last().pk,
                   "flag": choice.flag}
    else:
        response = {"next_question_text": choice.next_question.question_text,
                    "flag": choice.flag}
    data = json.dumps(response)
    return HttpResponse(data)