from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
]

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

def validate_dietary_restrictions(value):
    validate_choices(value, [choice.value for choice in DietaryRestrictions])

class HealthConditions(models.TextChoices):
    DIABETES = "Diabetes", _("Diabetes")
    HIGH_BLOOD_PRESSURE = "High Blood Pressure", _("High Blood Pressure")
    HIGH_CHOLESTEROL = "High Cholesterol", _("High Cholesterol")
    FOOD_ALLERGIES = "Food Allergies", _("Food Allergies")

def validate_health_conditions(value):
    validate_choices(value, [choice.value for choice in HealthConditions])
