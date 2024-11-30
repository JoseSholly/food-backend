from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),

]
class User(AbstractUser):

    email = models.EmailField(_('email address'), unique=True, )
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
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return self.email
    
    @property
    def full_name(self):
        return self.get_full_name()