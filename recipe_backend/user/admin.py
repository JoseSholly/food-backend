from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import WeightGoal, WeightLog
User = get_user_model()

class WeightLogInline(admin.TabularInline):
    model = WeightLog
    extra = 1


class WeightGoalInline(admin.StackedInline):
    model = WeightGoal
    extra = 1

@admin.register(User)
class CustomUserAdmin(auth_admin.UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_recipe_creator']
    search_fields = ('email', 'first_name', 'last_name')

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal Info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "bio",
                    "gender",
                    "age",
                    "date_of_birth",
                    "weight",
                    "height",
                    "profile_picture",
                    "is_recipe_creator",
                )
            },
        ),
        (
            _("Health Info"),
            {
                "fields": (
                    "streak",
                    "last_streak_date",
                    "activity_level",
                    "target_calories",
                    "bmi",
                    "bmi_category",
                    "target_weight",
                    "dietary_restrictions",
                    "health_conditions",
                    "nutritional_goals",
                    "lifestyle_preferences",
                    "has_completed_profile",
                )
            },
        ),
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
    inlines = [WeightGoalInline, WeightLogInline]
    
