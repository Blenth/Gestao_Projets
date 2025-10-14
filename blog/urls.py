# blog/urls.py
from django.urls import path
from . import views
#from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('', views.home, name='Home'),
    path('Login/', views.Login, name='Login'),  # rota raiz
    path('ListProduct/', views.List_Prooduct, name='ListOgject'),  # opcional
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