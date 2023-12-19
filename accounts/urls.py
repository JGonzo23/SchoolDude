# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_user),
    # Add other URL patterns as needed
]
