from django import forms
from .models import Pet


def external_valid_names(name):
    if name == "rex":
        raise forms.ValidationError("Nome muito ofensivo  ¯\_₍⸍⸌̣ʷ̣̫⸍̣⸌₎_/¯ !!!")


class PetForm(forms.ModelForm):
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        # external_valid_names(nome)
        if nome.upper() == 'PUTINHO':
            raise forms.ValidationError("Nome muito ofensivo  ¯\_₍⸍⸌̣ʷ̣̫⸍̣⸌₎_/¯ !!!")
        return nome

    class Meta:
        model = Pet
        fields = '__all__'
