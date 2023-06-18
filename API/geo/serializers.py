"""
Módulo que contém funções relacionadas aos serializers do Projeto.
"""

from rest_framework import serializers
from .models import Vagas


class VagasSerializer(serializers.ModelSerializer):
    """
    Serializador para a classe Vagas.
    """

    class Meta:
        """
        Classe Meta
        """
        model = Vagas
        fields = '__all__'

        def generic_method_vagas(self):
            """
            Método Generico
            """

        def generic_method_serializer(self):
            """
            Método Generico
            """


class VagasConversionSerializer(serializers.ModelSerializer):
    """
    Serializador para a conversão de campos geográficos da classe Vagas.
    """

    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    class Meta:
        """
        Classe Meta
        """
        model = Vagas
        fields = ['latitude', 'longitude', 'id']

        def generic_method_vagas(self):
            """
            Método vazio
            """

        def generic_method_conversion(self):
            """
            Método vazio
            """

    def get_latitude(self, instance):
        """
        Retorna a latitude da geometria da instância.
        """
        latitude = instance.geometry.y
        return latitude

    def get_longitude(self, instance):
        """
        Retorna a longitude da geometria da instância.
        """
        longitude = instance.geometry.x
        return longitude
