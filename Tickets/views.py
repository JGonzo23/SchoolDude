from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
import random, string
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from .form import TicketForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model

def ticket_home(request):
    return render(request,'home.html')


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect('ticket_list')  # Replace with the URL name for the ticket list view
    else:
        form = TicketForm()

    return render(request, 'create_ticket.html', {'form': form})

def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')  # Replace with the URL name for the ticket list view
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'edit_ticket.html', {'form': form, 'ticket': ticket})

def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')  # Replace with the URL name for the ticket list view

    return render(request, 'delete_ticket.html', {'ticket': ticket})

def ticket_list(request, location=None):
    if location:
        tickets = Ticket.objects.filter(location=location)
    else:
        tickets = Ticket.objects.all()

    return render(request, 'ticket_list.html', {'tickets': tickets, 'location':location})

class CreateTicketView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'create_ticket.html'
    success_url = '/tickets/'  # Redirect to the ticket list after successful creation

    def form_valid(self, form):
        # Assign the logged-in user to the created_by field
        if isinstance(self.request.user, get_user_model()):
            form.instance.created_by = self.request.user
            return super().form_valid(form)
        else:
            # Handle the case where the user is not an instance of CustomUser
            return self.form_invalid(form)
