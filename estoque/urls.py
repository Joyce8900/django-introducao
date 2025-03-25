from django.urls import path
from . import views  
urlpatterns = [
    path('cadastrar_produtos/', views.cadastrar_produtos, name='cadastrar_produtos'), 
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('deletar_produto/<int:id>', views.deletar_produto, name='deletar_produto'),
    path('editar_produto/<int:id>', views.editar_produto, name='editar_produto'),
    
]