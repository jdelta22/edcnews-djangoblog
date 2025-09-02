from django.shortcuts import render,get_list_or_404
from .models import Noticia, Categoria
# Create your views here.
def home(request):
    noticias = Noticia.objects.order_by('-data_publicacao')[:3]
    return render(request, 'edcnews/pages/home.html', context={'noticias': noticias})

def news_detail(request, news_id):
    noticia = Noticia.objects.get(id=news_id)
    return render(request, 'edcnews/pages/noticia.html', context={'noticia': noticia})

def all_news(request):
    noticias = Noticia.objects.order_by('-data_publicacao')
    return render(request, 'edcnews/pages/all-news.html', context={'noticias': noticias})

def category_news(request, category_id):
    noticias = get_list_or_404(Noticia.objects.filter(categoria__id=category_id).order_by('-id'))
    return render(request, 'edcnews/pages/category.html', context={
        'noticias': noticias,
        'categoria': noticias[0].categoria
        })