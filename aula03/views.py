from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


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


def show_code(request, code):
    html = f"<h1>O código é {code}</h1>"
    response = HttpResponse(html)
    return response


def http_cat(request, code):
    return HttpResponseRedirect(f"https://http.cat/{code}")


def show_get_values(request):
    # import ipdb;
    # ipdb.set_trace()
    nome = request.GET.get('nome', 'usuário anônimo')
    html = f"<h1>Bem vindo {nome}</h1>"
    return HttpResponse(html)


@csrf_exempt
def show_post_values(request):
    # import ipdb;
    # ipdb.set_trace()
    head = ""
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        head += f"<h1>Bem vindo {nome} {sobrenome}</h1>"

    html = f"""
    {head}
    <form method="post">
        <label for="nome">Nome:</label><br>
        <input type="text" id="nome" name="nome"><br>
        <label for="sobrenome">Sobrenome:</label><br>
        <input type="text" id="sobrenome" name="sobrenome"><br><br>
        <input type="submit" value="Submit">
    </form>
    """
    return HttpResponse(html)
