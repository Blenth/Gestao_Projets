# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # rota raiz
    path('home/', views.home, name='home'),  # opcional
    path('<int:id>/', views.produto_detail, name='produto_detail')
]
