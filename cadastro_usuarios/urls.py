# Django
from django.urls import path
# Views
from . import views

app_name = 'cadastro_usuarios'

urlpatterns = [
    path('', views.home, name='home'),
    path('cria_usuario/', views.cria_usuarios, name='cria_usuarios'), # type: ignore
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'), # type: ignore
    path('delete_usuario/', views.deleta_usuarios, name='delete_usuarios'), # type: ignore
]
