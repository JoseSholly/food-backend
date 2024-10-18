from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Recipe
from .serializers import RecipeSerializer

# class RecipeListCreateView(generics.ListCreateAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#     permission_classes = [IsAuthenticated]

# class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#     permission_classes = [IsAuthenticated]


from rest_framework import viewsets
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        cuisine = self.request.query_params.get('cuisine', None)
        course = self.request.query_params.get('course', None)
        
        if cuisine:
            queryset = queryset.filter(cuisine=cuisine)
        if course:
            queryset = queryset.filter(course=course)
            
        return queryset

@api_view(['GET'])
def search_recipes(request):
    query = request.query_params.get('q', '')
    if query:
        recipes = Recipe.objects.filter(food_name__icontains=query)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    return Response([])
