from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    twitter = models.URLField()
    data_nascimento = models.DateField(null=True)

    def __str__(self):
        return self.nome
