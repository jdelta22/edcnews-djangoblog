from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    cover = models.ImageField(upload_to='edcnews/images/%Y/%m/%d/', blank=True)
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descricao = models.CharField(max_length=200)
    conteudo = RichTextUploadingField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)  # contador de visualizações

    def __str__(self):
        return self.titulo
