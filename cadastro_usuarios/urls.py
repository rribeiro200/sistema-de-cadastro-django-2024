# Django
from django.urls import path
# Views
from . import views

app_name = 'cadastro_usuarios'

urlpatterns = [
    path('', views.home, name='home')
]
