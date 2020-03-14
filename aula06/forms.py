from django import forms
from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ("data_nascimento",)
