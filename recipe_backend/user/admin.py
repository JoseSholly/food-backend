from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for CustomUser model
    """
    model = User
    list_display = [
        'email', 'username', 'first_name', 
        'last_name', 'is_staff', 'is_recipe_creator'
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'profile_picture', 'date_of_birth', 'is_recipe_creator')}),
    )

admin.site.register(User, CustomUserAdmin)