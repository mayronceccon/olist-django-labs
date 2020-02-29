from django.db import models
from django.db.models import Sum


class Contato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    twitter = models.URLField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=254)
    texto = models.TextField()
    categorias = models.ManyToManyField(Categoria, related_name="posts")

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    autor = models.CharField(max_length=30)
    comentario = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comentário de {self.autor} no post {self.post}"


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.FloatField()

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    produtos = models.ManyToManyField(Produto, related_name="carrinhos")

    @property
    def total(self):
        return self.produtos \
            .aggregate(Sum('valor'))['valor__sum']
