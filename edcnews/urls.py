from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('all-news/', views.all_news, name='all_news'),
    path('category/<int:category_id>/', views.category_news, name='category_news'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
