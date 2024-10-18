from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)

class Recipe(models.Model):
    food_name = models.CharField(max_length=255)
    preparation_time = models.CharField(max_length=100)
    cooking_time = models.CharField(max_length=100)
    total_time = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    servings = models.IntegerField()
    calories = models.IntegerField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    preparation_instructions = models.TextField()

    def __str__(self):
        return self.food_name