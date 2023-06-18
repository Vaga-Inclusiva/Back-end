"""
Módulo que contém funções relacionadas aos Apps do Projeto
"""

from django.apps import AppConfig


class GeoConfig(AppConfig):
    """"
    Classe Geolocalização
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'geo'
