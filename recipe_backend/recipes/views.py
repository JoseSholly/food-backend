from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Recipe
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import RecipeCreateSerializer, RecipeDetailSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return RecipeCreateSerializer
        return RecipeDetailSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            recipe = self.perform_create(serializer)
            # Use DetailSerializer for the response
            response_serializer = RecipeDetailSerializer(recipe)
            
            return Response(
                {
                    'status': 'success',
                    'message': 'Recipe created successfully',
                    'data': response_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {
                    'status': 'error',
                    'message': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            recipe = self.perform_update(serializer)
            response_serializer = RecipeDetailSerializer(recipe)
            
            return Response(
                {
                    'status': 'success',
                    'message': 'Recipe updated successfully',
                    'data': response_serializer.data
                }
            )
        except Exception as e:
            return Response(
                {
                    'status': 'error',
                    'message': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def perform_update(self, serializer):
        return serializer.save()

@api_view(['GET'])
def search_recipes(request):
    query = request.query_params.get('q', '')
    if query:
        recipes = Recipe.objects.filter(food_name__icontains=query)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    return Response([])