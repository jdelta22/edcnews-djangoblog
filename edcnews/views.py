from django.shortcuts import render,get_list_or_404
from .models import Noticia
from utils.pagination import paginate_queryset

# Create your views here.
def home(request):
    noticias = Noticia.objects.order_by('-data_publicacao')[:3]
    return render(request, 'edcnews/pages/home.html', context={'noticias': noticias})

def news_detail(request, news_id):
    noticia = Noticia.objects.get(id=news_id)
    return render(request, 'edcnews/pages/noticia.html', context={'noticia': noticia})

def all_news(request):
    noticias = Noticia.objects.order_by('-data_publicacao')
    page_obj, page_range = paginate_queryset(request, noticias, per_page=5, around=2)
    return render(request, 'edcnews/pages/all-news.html', context={'noticias': page_obj, 'page_range': page_range})

def category_news(request, category_id):
    noticias = get_list_or_404(Noticia.objects.filter(categoria__id=category_id).order_by('-id'))
    page_obj, page_range = paginate_queryset(request, noticias, per_page=5, around=2)
    return render(request, 'edcnews/pages/category.html', context={
        'noticias': page_obj,
        'page_range': page_range,
        'categoria': noticias[0].categoria
        })

def search(request):
    query = request.GET.get("q", "").strip()

    results = Noticia.objects.none()

    if query:
        results = (Noticia.objects.filter(titulo__icontains=query) |
        Noticia.objects.filter(descricao__icontains=query) |
        Noticia.objects.filter(categoria__nome__icontains=query)
        ).order_by('-data_publicacao')

    results_page, page_range = paginate_queryset(request, results, per_page=5, around=2)
    
    
    return render(request, 'edcnews/pages/search.html', context={
        "query": query,
        "noticias": results_page,
        "page_range": page_range
    })

def about(request):
    return render(request, 'edcnews/pages/about.html')

def contact(request):
    return render(request, 'edcnews/pages/contact.html')
