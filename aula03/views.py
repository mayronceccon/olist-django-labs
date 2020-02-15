from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone


def index(request):
    html = "<h1>Bem vindo</h1>"
    response = HttpResponse(html, status=200)
    response['Ultimo-Acesso'] = timezone.localtime(timezone.now())
    return response


def setacookie(request):
    respose = HttpResponse()
    respose.set_cookie('my_name', value="Mayron")
    return respose


def redireciona(request):
    return HttpResponseRedirect("https://dev.to")
