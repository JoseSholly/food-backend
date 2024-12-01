from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(auth_admin.UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff', 'is_recipe_creator']
    search_fields = ('email', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_("Personal Info"), {"fields": ("username","first_name", "last_name", "bio", "gender","date_of_birth", "profile_picture", "is_recipe_creator")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        
        
        )
    
