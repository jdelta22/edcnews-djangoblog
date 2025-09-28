from django.core.paginator import Paginator

def paginate_queryset(request, queryset, per_page=10, around=2):
    """
    Pagina um queryset e retorna:
      - page_obj: objeto da página atual
      - page_range_custom: intervalo de páginas limitado (com base em 'around')

    Args:
        request: HttpRequest
        queryset: queryset a ser paginado
        per_page: quantos itens por página
        around: quantos números antes/depois da página atual mostrar
    """
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # calcula intervalo numérico de páginas
    start = max(page_obj.number - around, 1)
    end = min(page_obj.number + around, paginator.num_pages) + 1
    page_range_custom = range(start, end)

    return page_obj, page_range_custom