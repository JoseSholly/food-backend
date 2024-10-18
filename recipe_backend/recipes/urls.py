from django.urls import path
from . import views

# urlpatterns = [
#     path('recipes/', views.RecipeListCreateView.as_view(), name='recipe-list'),
#     path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', views.search_recipes, name='search-recipes'),
]
