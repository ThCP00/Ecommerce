from django.urls import path
from . import views


urlpatterns = [
    path("salvar_perfil", views.salvar_perfil, name='salvar_perfil'),
    path("perfil", views.perfil, name='perfil'),
]