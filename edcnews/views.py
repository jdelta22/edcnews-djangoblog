from django.shortcuts import render,get_list_or_404
from .models import Noticia
from utils.pagination import paginate_queryset
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import NoticiaForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import uuid
# Create your views here.
def home(request):
    noticias = Noticia.objects.order_by('-data_publicacao')[:3]
    pafinator = Paginator(noticias, 5)
    page_obj = pafinator.get_page(1)
    return render(request, 'edcnews/pages/home.html', context={
        'noticias': page_obj.object_list,
        page_obj: page_obj})

def load_more_news(request):
    page = int(request.GET.get("page", 2))

    noticias = Noticia.objects.all().order_by("-data_publicacao")
    paginator = Paginator(noticias, 5)
    page_obj = paginator.get_page(page)

    html = render_to_string("edcnews/partials/news-itens.html", {
        "noticias": page_obj.object_list
    })

    return JsonResponse({
        "has_next": page_obj.has_next(),
        "html": html,
    })


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

def criar_noticia(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NoticiaForm()

    return render(request, "edcnews/pages/criar-noticia.html", {"form": form})

@csrf_exempt
def upload_imagem(request):
    if request.method == "POST" and request.FILES.get("image"):
        arquivo = request.FILES["image"]
        nome = f"tiptap/{uuid.uuid4()}_{arquivo.name}"

        caminho = default_storage.save(nome, arquivo)
        url = default_storage.url(caminho)

        return JsonResponse({"url": url})

    return JsonResponse({"error": "no image"}, status=400)