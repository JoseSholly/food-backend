"""recipe_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from django.urls import path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.schemas import get_schema_view as get_restframe_work_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Recipe API",
        default_version="v1",
        description="This API provides endpoints for managing recipes, ingredients, and related operations.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('recipes.urls')),
    path('api/v1/', include('user.urls')),
    

    # Documentation Urls
    path("api-schema/", get_restframe_work_schema(title="API Schema", description="Guide for the Inverter Power REST API"), name="api_schema"),
    path('api/v1/docs/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #  Token Authentication
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


