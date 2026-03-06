from django.contrib import admin

from .models import Author


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Campos que aparecerão na lista principal
    list_display = ("name", "user", "email")

    # Permite clicar no nome ou no usuário para editar
    list_display_links = ("name", "user")

    # Adiciona uma barra de pesquisa
    search_fields = ("name", "email", "user__username")

    # Organiza os campos dentro da página de edição
    fieldsets = (
        (
            "Informações Pessoais",
            {"fields": ("user", "name", "email", "profile_picture")},
        ),
        (
            "Sobre o Autor",
            {
                "fields": ("bio",),
            },
        ),
    )
