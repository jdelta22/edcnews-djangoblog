from django.urls import path

from .views import (
    Dashboard,
    Login,
    NoticiaCreateView,
    NoticiaDeleteView,
    NoticiaUpdateView,
)

app_name = "authors"
urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("create/", NoticiaCreateView.as_view(), name="create"),
    path("update/<int:pk>/", NoticiaUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", NoticiaDeleteView.as_view(), name="delete"),
]
