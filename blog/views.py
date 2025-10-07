# blog/views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Produto


def home(request):
    return render(request, 'listProduct.html')  # ou qualquer template que você tenha

def produto_detail(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produtos/inforProduct.html', {'produto': produto})