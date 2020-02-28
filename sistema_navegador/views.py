from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # (?:Mozilla\/[0-9].[0-9]\s\()(?P<sistema>.*?)(?:\)\s)(?P<navegador>.*)(?:\(.*|)
    return HttpResponse(request.META['HTTP_USER_AGENT'])
