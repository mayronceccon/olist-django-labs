from django.shortcuts import render, get_object_or_404
from .models import Contato
from .forms import ContatoForm


def index(request):
    form = ContatoForm()

    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()

    contatos = Contato.objects.all()
    contexto = {
        "form": form,
        "contatos": contatos,
    }
    return render(request, "aula06/index.html", context=contexto)


def edit(request, id):
    contato = get_object_or_404(Contato, pk=id)

    form = ContatoForm(
        initial={
            "nome": contato.nome,
            "email": contato.email,
            "twitter": contato.twitter,
        }
    )

    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save(instance=contato)

    contatos = Contato.objects.all()
    contexto = {
        "form": form,
        "contatos": contatos,
    }
    return render(request, "aula06/index.html", context=contexto)
