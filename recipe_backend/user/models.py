from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from datetime import timedelta
from django.utils.timezone import now
import uuid


GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),

]
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True, )
    username = models.CharField(max_length=150, blank=True, null=True, unique=False)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        null=True, 
        blank=True,
        help_text=_("The profile picture of the user.")
    )
    date_of_birth = models.DateField(null=True, blank=True, help_text=_("Date of birth of user"))
    gender = models.CharField(choices= GENDER, max_length=10,null=True, default=None, help_text=_("The gender of user"))

    is_recipe_creator = models.BooleanField(default=False, help_text= _("Designates if user is allowed to create recipe"))
    # clerk_id = models.CharField(max_length=255, unique=True)
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_("User age"),
    )
    height = models.FloatField(
        null=True,
        blank=True,
        help_text=_("User height"),
    )
    weight = models.FloatField(
        null=True,
        blank=True,
        help_text=_("Weight of user"),
    )
    activity_level = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Activity level of user"),
    )
    target_calories = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_("Calories target set by user"),
    )
    created_at = models.DateTimeField(
        default=now,
        editable=False,
        help_text=_("Time usr was created"),
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text=_("Last time user update model")
    )
    last_streak_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text=_("User last streak date"),
    )
    bmi = models.FloatField(
        null=True,
        blank=True,
        help_text=_("Body Mass index of user"),
    )
    bmi_category = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("BMI category"),
    )
    target_weight = models.FloatField(
        null=True,
        blank=True,
        help_text=_("Weight target set by user"),
    )
    streak = models.PositiveIntegerField(
        default=0, help_text=_("User streak")
    )
    dietary_restrictions = models.JSONField(default=list, blank=True, help_text=_("Dietary restrictions of user"))
    health_conditions = models.JSONField(default=list, blank=True, help_text=_("Health conditions of user"))
    nutritional_goals = models.JSONField(default=list, blank=True, help_text=_("Nutritional goals of user"))
    lifestyle_preferences = models.JSONField(default=list, blank=True, help_text=_("Lifestyle preferences of user"))
    has_completed_profile = models.BooleanField(default=False, help_text=_("Designates if user has completed profile"))


    

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    
    # Override the default username field to use email for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    @property
    def full_name(self):
        return self.get_full_name()


class WeightLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="weight_logs")
    weight = models.FloatField()
    logged_at = models.DateTimeField(default=now, editable=False, help_text=_("Time weight was logged"))

    def __str__(self):
        return f"{self.user}: {self.weight} kg at {self.logged_at}"


class WeightGoal(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="weight_goal"
    )
    goal_weight = models.FloatField(help_text=_("The weight user wants to achieve"))
    deadline = models.DateField(null=True, blank=True, help_text=_("The deadline for achieving the goal"))

    def __str__(self):
        return f"{self.user}: Goal {self.goal_weight} kg by {self.deadline}"


class PasswordResetToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="password_reset_token")
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'is_used')

    def is_valid(self):
        return now() - self.created_at < timedelta(hours=1)  # Token valid for 1 hour