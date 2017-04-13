from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
import json

def handle_index(request):
    return render(request, "game/index.html")

@csrf.csrf_exempt
def handle_ajax(request):
    request='POST'
    return HttpResponse("Hello there")