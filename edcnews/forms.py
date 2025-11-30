from django import forms
from .models import Noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        # Include all fields you want to be editable in the form
        fields = [
            'cover',
            'titulo',
            'slug',
            'descricao',
            'conteudo',
            'categoria'
        ]
