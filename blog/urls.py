from django.urls import path
from . import views
from .views import List_Product
urlpatterns = [
    path('', views.home, name='Home'),
    path('Login/', views.Login, name='Login'),
    path('ListProduct/', List_Product, name='ListOgject'),
    path('produto/<str:nome>/<path:imagem>/', views.exibir_produto, name='ListObject'),
]