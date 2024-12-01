from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'bio', 'profile_picture', 'date_of_birth', 'is_recipe_creator']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'bio', 'profile_picture', 'date_of_birth', 'is_recipe_creator']
