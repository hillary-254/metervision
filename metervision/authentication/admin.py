from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from .models import UserProfile

# Register the UserProfile model
admin.site.register(UserProfile, UserAdmin)

