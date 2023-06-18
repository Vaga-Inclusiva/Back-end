"""
Módulo que contém funções relacionadas ao swagger
"""

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path

SchemaView = get_schema_view(
    openapi.Info(
        title="VagaInclusiva-API",
        default_version='v1',
        description="API da aplicação VagaInclusiva",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        'swagger(<format>.json|.yaml)',
        SchemaView.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        SchemaView.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        SchemaView.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
