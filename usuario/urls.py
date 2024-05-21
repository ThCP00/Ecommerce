from . import views
from django.urls import path, include


urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('realizar_login/', views.realizar_login, name='realizar_login'),
    path('sair/', views.sair, name='sair'),
]
