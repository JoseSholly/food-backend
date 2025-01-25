from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
]

def validate_dietary_restrictions(value):
    validate_choices(value, [choice.value for choice in DietaryRestrictions])


def validate_choices(value, choices):
    if not all(item in choices for item in value):
        raise ValidationError(_("Invalid choice: %(value)s"), params={"value": value})

class DietaryRestrictions(models.TextChoices):
    VEGETARIAN = "Vegetarian", _("Vegetarian")
    VEGAN = "Vegan", _("Vegan")
    GLUTEN_FREE = "Gluten-free", _("Gluten-free")
    LACTOSE_INTOLERANT = "Lactose Intolerant", _("Lactose Intolerant")
    HALAL = "Halal", _("Halal")
    KOSHER = "Kosher", _("Kosher")

HEALTH_CONDITIONS_CHOICES = [
    ("Diabetes", "Diabetes"),
    ("High Blood Pressure", "High Blood Pressure"),
    ("High Cholesterol", "High Cholesterol"),
    ("Food Allergies", "Food Allergies"),
]

NUTRITIONAL_GOALS_CHOICES = [
    ("Weight Loss", "Weight Loss"),
    ("Weight Gain", "Weight Gain"),
    ("Muscle Building", "Muscle Building"),
    ("Endurance Training", "Endurance Training"),
]

LIFESTYLE_PREFERENCES_CHOICES = [
    ("Busy Schedule", "Busy Schedule"),
    ("Beginner Cooking Skills", "Beginner Cooking Skills"),
    ("Intermediate Cooking Skills", "Intermediate Cooking Skills"),
    ("Advanced Cooking Skills", "Advanced Cooking Skills"),
    ("Spicy Food", "Spicy Food"),
    ("Sweet Food", "Sweet Food"),
    ("Savory Food", "Savory Food"),
]
