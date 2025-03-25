from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produto
def cadastrar_produtos(request):
    if request.method == 'GET':
        return render(request,'cadastrar_produtos.html')
    elif request.method == 'POST':
        nome1 = request.POST.get('nome')
        quantidade1 = request.POST.get('quantidade')
        preco1 = request.POST.get('preco')
        fabricacao1 = request.POST.get('fabricacao')

        produto = Produto(nome=nome1,quantidade=quantidade1,preco=preco1,fabricacao=fabricacao1)

        produto.save()
        return redirect('listar_produtos')
                            
        

def listar_produtos(request):
    produtos = Produto.objects.all()
    preco = request.GET.get('preco')
    if preco:
        produtos = produtos.filter(preco__gt=preco)
    return render(request,'listar_produtos.html', {'produtos':produtos})

def deletar_produto(request,id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('listar_produtos')

def editar_produto(request,id):
    produto = get_object_or_404(Produto,id=id)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.quantidade = request.POST.get('quantidade')
        produto.preco = request.POST.get('preco')
        produto.fabricacao = request.POST.get('fabricacao')
        produto.save()
        return redirect('listar_produtos')
    
    produto = {
            'id':produto.id,
            'nome':produto.nome,
            'quantidade':produto.quantidade,
            'preco':produto.preco,
            'fabricacao':produto.fabricacao
        }
    
    return render(request,'editar_produto.html', {'produto':produto})
    

