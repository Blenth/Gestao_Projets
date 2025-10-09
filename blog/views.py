# blog/views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Produto


def home(request):
    return render(request, 'base.html')

def Login(request):
    return render(request, 'base.html')

def List_Prooduct(request):
    return render(request, 'listProduct.html')  # ou qualquer template que você tenha


def exibir_produto(request, numero):
    contexto = {'numero_produto': numero}
    return render(request, 'produto.html', contexto)