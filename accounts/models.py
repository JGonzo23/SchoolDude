from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, location=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)

        # Check the user type
        user_type = extra_fields.pop('user_type', 'regular')

        if user_type == 'admin':
            # Create a superuser
            return self.create_superuser(email, username, password, location, **extra_fields)
        else:
            # Create a regular user
            user = self.model(email=email, username=username, user_type=user_type, location=location, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_staff_user(self, email, username, password=None, location=None, **extra_fields):
        # Create a staff user with the default user type as 'staff'
        return self.create_user(email, username, password, location, user_type='staff', **extra_fields)

    def create_tech_user(self, email, username, password=None, location=None, **extra_fields):
        # Create a tech user with the default user type as 'tech'
        return self.create_user(email, username, password, location, user_type='tech', **extra_fields)

    def create_superuser(self, email, username, password=None, location=None, **extra_fields):
        # Ensure a strong password is provided for superusers
        if password is None:
            raise ValueError('Superuser must have a password')

        # Call the create_user method to handle common user creation logic
        user = self.create_user(email, username, password, location, **extra_fields)

        # Set additional fields for a superuser
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser, PermissionsMixin):
    USER_TYPES = (
        ('tech', 'Tech'),
        ('staff', 'Staff'),
        ('admin', 'Admin')
    )

    LOCATIONS = (
        ('WIS', 'WIS'),
        ('LINCOLN', 'Lincoln'),
        ('DHS', 'DHS'),
        ('JEFFERSON', 'JEFFERSON'),
        ('GRANDVIEW', 'GRANDVIEW'),
        ('WILSON', 'WILSON'),
        ('JFK', 'JFK'),
        ('ROOSEVELT', 'ROOSEVELT'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='regular')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    location = models.CharField(max_length=20, choices=LOCATIONS, default='DHS')

    # ... other fields ...

    # Use the custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.email

class TechUserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    tech_field_1 = models.CharField(max_length=50)
    tech_field_2 = models.IntegerField()
    # Add any additional fields specific to TechUser

    def __str__(self):
        return self.user.email