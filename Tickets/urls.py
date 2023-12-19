from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.ticket_home),
    path('ticketsh/', views.ticket_list, name='ticket_list'),
    path('tickets/<str:location>/', views.ticket_list, name='ticket_list_by_location'),
    path('create/', views.create_ticket, name='create_ticket'),

]