from django.urls import path
from . import views

urlspatterns = [
  path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
]
