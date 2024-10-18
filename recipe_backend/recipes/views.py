from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import generics
from .models import Recipe,Ingredient
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


            # recipe = self.perform_update(serializer)
            # response_serializer = RecipeDetailSerializer(recipe)
             # Handle the ingredients in the update process
            ingredients_data = serializer.validated_data.pop('ingredients', [])
            
            # Update the recipe instance
            recipe = self.perform_update(serializer)
            
            # Clear existing ingredients and create new ones
            recipe.ingredients.clear()
            for ingredient_data in ingredients_data:
                ingredient = Ingredient.objects.create(**ingredient_data)
                recipe.ingredients.add(ingredient)
            
            response_serializer = RecipeDetailSerializer(recipe)  # Use DetailSerializer for response
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

# @api_view(['GET'])
# def search_recipes(request):
#     query = request.query_params.get('q', '')
#     if query:
#         recipes = Recipe.objects.filter(food_name__icontains=query)
#         serializer = RecipeDetailSerializer(recipes, many=True)
#         return Response(serializer.data)
#     return Response([])

class SearchRecipesView(generics.GenericAPIView):
    serializer_class = RecipeDetailSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '')
        if query:
            recipes = Recipe.objects.filter(food_name__icontains=query)
            serializer = self.get_serializer(recipes, many=True)
            return Response(serializer.data)
        return Response([])
