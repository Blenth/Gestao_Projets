# blog/urls.py
from django.urls import path
from . import views
#from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('', views.home, name='home'),  # rota raiz
    path('home/', views.home, name='home'),  # opcional
    path('<int:id>/', views.produto_detail, name='produto_detail')
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