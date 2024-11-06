import os
from django.db import models

MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('stressed', 'Stressed'),
        ('relaxed', 'Relaxed'),
    ]

WEATHER_CHOICES = [
        ('sunny', 'Sunny'),
        ('rainy', 'Rainy'),
        ('cloudy', 'Cloudy'),
    ]
ENERGY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

HUNGER_CHOICES = [
        ('snack', 'Snack'),
        ('meal', 'Meal'),
        ('full', 'Full'),
    ]

BUDGET_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very high', 'Very High'),
    ]
DIETARY_CHOICES = (
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('gluten-free', 'Gluten-Free'),
        ('dairy-free', 'Dairy-Free'),
    )
    
ALLERGY_CHOICES = (
        ('nuts', 'Nuts'),
        ('dairy', 'Dairy'),
        ('eggs', 'Eggs'),
        ('soy', 'Soy'),
    )


  
def recipe_image_path(instance, filename):
    # Extract file extension from the original filename
    ext = filename.split('.')[-1]
    # Construct new filename using food_name and extension
    filename = f"{instance.food_name}_{instance.cuisine}.{ext}"
    # Return the full path where the image will be uploaded
    return os.path.join('recipe_images/', filename)
