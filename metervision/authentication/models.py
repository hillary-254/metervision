# authentication/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    # Add any additional fields you want to include in your user model
    # For example:
    # profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',  # Added related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',  # Added related_name
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username
