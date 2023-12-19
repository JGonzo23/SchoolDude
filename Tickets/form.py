from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'location', 'created_by']
       
        # You can customize the form fields as needed

def clean_created_by(self):
    return self.instance.created_by if self.instance else self.fields['created_by'].initial