from django.db import models
from django.contrib.auth.models import User
from Accounts.models import CustomUser

class TicketStatus(models.TextChoices):
    TO_DO = 'To Do'
    IN_PROGRESS = 'In Progress'
    IN_REVIEW = 'In Review'
    DONE = 'Done'
    
    
class TicketType(models.Model):
    title = models.CharField(max_length=50)    

class PriorityChoices(models.TextChoices):
    LOW = 'low'
    MEDIUM = 'Medium'
    HIGH = 'high'
    
class Ticket(models.Model):
    title = models.CharField(max_length=100)
    tech_assigned = models.ForeignKey(CustomUser,on_delete=models.PROTECT,related_name = 'tech_assigned')
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
    description = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete = models.PROTECT, related_name = 'created_by')
    location = models.CharField(max_length=20, choices=CustomUser.LOCATIONS, null=True, blank=True)
    priority = models.CharField(max_length = 25, choices = PriorityChoices.choices, default = PriorityChoices.MEDIUM)
    ticket_type = models.ForeignKey(TicketType, on_delete = models.PROTECT)