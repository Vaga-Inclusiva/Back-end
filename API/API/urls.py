"""
Módulo que contém funções relacionadas as rotas do Projeto
"""

from django.contrib import admin
from django.urls import path, include
# pylint: disable=import-error
from geo.views import VagasAPIView
from .swagger import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('vagas/', VagasAPIView.as_view()),
    path('', include(swagger_urls)),
]
