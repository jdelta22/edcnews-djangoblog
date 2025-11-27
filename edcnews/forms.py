from django import forms
from .models import Noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "cover", "conteudo"]
        widgets = {
            "conteudo": forms.HiddenInput(),  # TipTap preenche
        }