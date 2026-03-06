import bleach
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from authors.models import Author

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    cover = models.ImageField(upload_to="edcnews/images/%Y/%m/%d/", blank=True)
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descricao = models.CharField(max_length=200)
    conteudo = RichTextUploadingField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="noticias"
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)  # contador de visualizações

    def save(self, *args, **kwargs):
        # 1. TAGS PERMITIDAS
        # Mantemos apenas o essencial para a sua barra de ferramentas Custom
        allowed_tags = [
            "p",
            "b",
            "i",
            "u",
            "em",
            "strong",
            "a",
            "ul",
            "ol",
            "li",
            "br",
            "img",
            "blockquote",
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "div",
            "span",  # Necessários para alinhamento e formatos do CKEditor
        ]

        # 2. ATRIBUTOS PERMITIDOS
        allowed_attrs = {
            "a": ["href", "title", "target"],
            "img": ["src", "alt", "width", "height", "style", "class"],
            "div": ["style", "class"],  # CKEditor usa divs para Justify (alinhamento)
            "p": ["style", "class"],
            "span": ["style", "class"],
            "*": ["class"],  # Permite classes CSS em qualquer tag permitida
        }

        # 3. ESTILOS CSS PERMITIDOS
        # Focado em alinhamento e dimensões de imagem
        allowed_styles = ["text-align", "width", "height", "margin", "float", "padding"]

        # 4. LIMPEZA
        # O strip=True garante que <script> ou <iframe> sejam DELETADOS, não apenas escapados.
        clean_html = bleach.clean(
            self.conteudo,
            tags=allowed_tags,
            attributes=allowed_attrs,
            styles=allowed_styles,
            strip=True,
        )

        self.conteudo = clean_html
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
