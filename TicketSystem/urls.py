from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.ticket_home)
]