# blog/urls.py
from django.urls import path
from . import views
from .views import List_Product
#from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('', views.home, name='Home'),
    path('Login/', views.Login, name='Login'),
    path('ListProduct/', List_Product, name='ListOgject'),
    path('produto/<str:lanche>/', views.exibir_produto, name='exibir_produto')
]
    
'''
urlpatterns = [
        # ... other URL patterns
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI views
        path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
'''