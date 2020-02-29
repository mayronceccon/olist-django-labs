from django.shortcuts import render


def index(request):
    return render(request, "aula04/index.html")
