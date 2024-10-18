from rest_framework import serializers
from .models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['food_name', 'preparation_time', 'cooking_time', 'total_time', 'course', 'cuisine', 'servings', 'calories', 'ingredients', 'preparation_instructions']
