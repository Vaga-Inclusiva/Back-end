"""
Módulo que contém funções relacionadas às views do Projeto
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db import models  # Importando o módulo models
from .serializers import VagasConversionSerializer

class VagasAPIView(APIView):
    """
    View para retornar as vagas com base em coordenadas de latitude e longitude.
    """

    def get(self, request):
        """
        Método GET para obter as vagas com base nas coordenadas de latitude e longitude fornecidas.
        """
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')

        point = Point(float(longitude), float(latitude), srid=4326)

        locais = Vagas.objects.filter(geometry__distance_lte=(point, D(km=1)))

        serializer = VagasConversionSerializer(locais, many=True)

        return Response(serializer.data)

class Vagas(models.Model):
    """
    Modelo que representa as vagas.
    """

    # campos e definições do modelo

    objects = models.Manager()  # Adicionado o gerenciador 'objects'
