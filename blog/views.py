# blog/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'listProduct.html')  # ou qualquer template que você tenha
