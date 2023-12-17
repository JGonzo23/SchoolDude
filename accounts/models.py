from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('tech', 'Tech'),
        ('regular', 'Regular User'),
    )
    
    LOCATIONS = (
        ('WIS', 'WIS',),
        ('LINCOLN', 'Lincoln'),
        ('DHS', 'DHS'),
        ('JEFFERSON', 'JEFFERSON'),
        ('GRANDVIEW', 'GRANDVIEW'),
        ('WILSON', 'WILSON'),
        ('JFK','JFK'),
        ('ROOSEVELT', 'ROOSEVELT'),
        
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='regular')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    location = models.CharField(max_length=20, choices = LOCATIONS, default = 'DHS')


    # Add any additional fields you need for your user





