from django.shortcuts import render


def index(request):
    context = {
        "alunos": [
            "Mayron",
            "Pedro",
            "João",
        ]
    }
    return render(request, "aula04/index.html", context=context)
