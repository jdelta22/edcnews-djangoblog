from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from edcnews.models import Noticia

from .forms import NoticiaForm

# Create your views here.


class Login(LoginView):
    template_name = "authors/pages/login.html"

    def get_success_url(self):
        return reverse_lazy("authors:dashboard")


class Dashboard(LoginRequiredMixin, ListView):
    template_name = "authors/pages/profile.html"
    context_object_name = "noticias"

    def get_queryset(self):
        return self.request.user.author.noticias.all().order_by("-data_publicacao")


class NoticiaCreateView(LoginRequiredMixin, CreateView):
    # 1. Modelo: O modelo que esta view irá criar
    model = Noticia

    # 2. Formulário: A classe de formulário que contém o CKEditor
    form_class = NoticiaForm

    # 3. Template: O arquivo HTML a ser renderizado
    template_name = "edcnews/pages/criar-noticia.html"

    # 4. URL de Sucesso: Para onde redirecionar após o sucesso
    success_url = reverse_lazy("authors:dashboard")

    # 5. Lógica de Validação (Obrigatória para definir o Autor)
    def form_valid(self, form):
        # Define o campo 'author' para o usuário logado antes de salvar
        form.instance.author = self.request.user.author
        return super().form_valid(form)


class NoticiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = "edcnews/pages/editar.html"
    success_url = reverse_lazy("authors:dashboard")


class NoticiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Noticia
    success_url = reverse_lazy("authors:dashboard")

    def get_queryset(self):
        return self.request.user.author.noticias.all()

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["POST"])

    def form_valid(self, form):
        messages.success(self.request, "Notícia deletada com sucesso!")
        return super().form_valid(form)
