from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation 
from django.contrib.contenttypes.models import ContentType

from DistrictTag.models import TaggedItem



class TicketType(models.Model):
    title = models.CharField(max_length=255)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType,on_delete = models.PROTECT)
    object_id = models.PositiveIntegerField()
    tag = GenericForeignKey('content_type', 'object_id')
    
    

class BaseTicket(models.Model):
    OPEN = 'Open'
    IN_PROGRESS = 'In Progress'
    RESOLVED = 'Resolved'
    CLOSED = 'Closed'

    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (IN_PROGRESS, 'In Progress'),
        (RESOLVED, 'Resolved'),
        (CLOSED, 'Closed'),
    ]

    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]
    
    customer = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)
    ticket_description = GenericRelation(TaggedItem, related_query_name='ticket_descriptions')
    attachments = GenericRelation(TaggedItem, related_query_name='ticket_attachments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=OPEN)
    ticket_title = models.CharField(max_length=255)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default=MEDIUM)
    location = models.CharField(max_length=225)
    assigned_technician = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name= 'assigned_tech')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    ticket_id = models.CharField(max_length = 15, unique = True)
    is_assigned_to_tech = models.BooleanField(default = False)
    slug = models.SlugField(default='-')
    
class StatusChange(models.Model):
    ticket = models.ForeignKey(BaseTicket, on_delete=models.CASCADE)
    from_status = models.CharField(max_length=20, choices=BaseTicket.STATUS_CHOICES)
    to_status = models.CharField(max_length=20,choices=BaseTicket.STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    
class ActivityLog(models.Model):
    ticket = models.ForeignKey(BaseTicket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    time_worked_minutes = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.user} - {self.action} on {self.ticket} at {self.timestamp}"   
    
class Customer(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)\
            
         
         
       
