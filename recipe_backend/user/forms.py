from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
from .models import User
from .utils import DietaryRestrictions, HealthConditions
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomUserChangeForm(UserChangeForm):
    dietary_restrictions = forms.MultipleChoiceField(
        choices=DietaryRestrictions.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text=_("Dietary restrictions of user")
    )
    health_conditions = forms.MultipleChoiceField(
        choices=HealthConditions.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text=_("Health conditions of user"),
    )

    nutritional_goals = forms.MultipleChoiceField(
        choices=HealthConditions.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text=_("Health conditions of user"),
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'bio', 'profile_picture', 'date_of_birth', 'is_recipe_creator']

    def clean_dietary_restrictions(self):
        return self.cleaned_data.get("dietary_restrictions", [])

    def clean_health_conditions(self):
        return self.cleaned_data.get("health_conditions", [])
    
    def clean_nutritional_goals(self):
        return self.cleaned_data.get("nutritional_goals", [])

class CustomUserCreationForm(UserCreationForm):
    dietary_restrictions = forms.MultipleChoiceField(
        choices=DietaryRestrictions.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text=_("Health conditions of user")
    )

    health_conditions = forms.MultipleChoiceField(
        choices=HealthConditions.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text=_("Health conditions of user"),
    )

    nutritional_goals = forms.MultipleChoiceField(
        choices=HealthConditions.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text=_("Health conditions of user"),
    )
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'bio', 'profile_picture', 'date_of_birth', 'is_recipe_creator']

    def clean_dietary_restrictions(self):
        return self.cleaned_data.get("dietary_restrictions", [])

    def clean_health_conditions(self):
        return self.cleaned_data.get("health_conditions", [])
    
    def clean_nutritional_goals(self):
        return self.cleaned_data.get("nutritional_goals", [])

