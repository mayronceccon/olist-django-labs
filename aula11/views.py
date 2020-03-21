from django.shortcuts import render
from .models import Post


def aula11(request):
    posts = Post.objects.select_related("categoria").all()
    return render(request, "aula11/index.html", {"posts": posts})
