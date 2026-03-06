from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from edcnews.models import Noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        # Include all fields you want to be editable in the form
        fields = ["cover", "titulo", "slug", "descricao", "conteudo", "categoria"]


class AuthorRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, label="Nome Completo")
    email = forms.EmailField(label="E-mail")
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(
        label="Foto de Perfil",
        required=False,
        widget=forms.FileInput(),  # Para ficar limpo no estilo login
    )

    class Meta(UserCreationForm.Meta):
        model = User  # O formulário base ainda cria o User
        fields = UserCreationForm.Meta.fields + ("email",)

    field_order = [
        "profile_picture",  # 1º Foto
        "username",  # 2º Username (campo padrão do UserCreationForm)
        "name",  # 3º Nome completo
        "email",  # 4º E-mail
        "password1",  # 5º Senha (campo padrão)
        "password2",  # 6º Confirmação de senha (campo padrão)
        "bio",  # 7º Bio (opcional, deixei por último)
    ]
