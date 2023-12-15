from django import forms
from .models import BaseTicket
import random
import string

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = BaseTicket
        fields = ['ticket_title', 'ticket_ description', 'ticket_id']