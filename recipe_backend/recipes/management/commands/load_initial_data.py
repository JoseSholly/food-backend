from django.core.management.base import BaseCommand
import json
from recipes.models import Recipe, Ingredient

class Command(BaseCommand):
    help = 'Load initial recipe data'

    def handle(self, *args, **kwargs):
        with open('foods.json') as f:
            data = json.load(f)
            
        for recipe_data in data['recipes']:
            # Create recipe
            recipe = Recipe.objects.create(
                food_name=recipe_data['food_name'],
                preparation_time=recipe_data['preparation_time'],
                cooking_time=recipe_data['cooking_time'],
                total_time=recipe_data['total_time'],
                course=recipe_data['course'],
                cuisine=recipe_data['cuisine'],
                servings=recipe_data['servings'],
                calories=recipe_data['calories'],
                preparation_instructions=recipe_data['preparation_instructions']
            )
            
            # Create ingredients
            for ingredient_data in recipe_data['ingredients']:
                ingredient = Ingredient.objects.create(
                    name=ingredient_data['name'],
                    quantity=ingredient_data['quantity']
                )
                recipe.ingredients.add(ingredient)