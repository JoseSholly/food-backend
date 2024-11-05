from rest_framework import serializers
from .models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']

class RecipeCreateSerializer(serializers.ModelSerializer):
    # ingredients = serializers.ListField(
    #     child=serializers.DictField(
    #         child=serializers.CharField()
    #     ),
    #     write_only=True
    # )
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'food_name','image','preparation_time', 'cooking_time', 
                 'total_time', 'course', 'cuisine', 'servings', 'calories',
                 'ingredients', 'preparation_instructions']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        
        # Create ingredients for the recipe
        for ingredient_data in ingredients_data:
            ingredient = Ingredient.objects.create(
                name=ingredient_data.get('name', ''),
                quantity=ingredient_data.get('quantity', '')
            )
            recipe.ingredients.add(ingredient)
        
        return recipe
        

class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'food_name','image' ,'preparation_time', 'cooking_time', 
                 'total_time', 'course', 'cuisine', 'servings', 'calories',
                 'ingredients', 'preparation_instructions' ]