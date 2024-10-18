from django.contrib import admin
from .models import Recipe, Ingredient

# Registering the Ingredient model
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id','name','get_recipes',)  # Display these fields in the admin list view
    search_fields = ('name',)  # Add a search box for the name field

    def get_recipes(self, obj):
        # Get a comma-separated list of recipe names
        return ', '.join([recipe.food_name for recipe in obj.recipe_set.all()])
    get_recipes.short_description = 'Recipes'  # Set column title


# Registering the Recipe model
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id','food_name', 'course', 'cuisine', 'servings', 'calories')  # Display these fields in the admin list view
    search_fields = ('food_name', 'course', 'cuisine')  # Add a search box for specified fields
    list_filter = ('course', 'cuisine')  # Add filters for course and cuisine
    ordering = ('food_name',)  # Default ordering of the recipes

