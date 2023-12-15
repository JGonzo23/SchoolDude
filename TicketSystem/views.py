from django.shortcuts import render, redirect
from django.contrib import messages
from .form import CreateTicketForm
from .models import BaseTicket
from django.db import IntegrityError
import random, string

#can create ticket form here
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.customer = request.user
            while not var.ticket_id:
                id = ''.join(random.choices(string.digits, k=6))
                try:
                    var.ticket_id = id
                    var.save()
                    break
                except IntegrityError:
                    continue
            messages.success(request='Your ticket has been submitted. A technician will reach out soon')
            return redirect('customer-tickets')
        else:
            messages.warning(request, 'Something went wrong. Please check for errors')
            return redirect('create-ticket')
    else: 
        form = CreateTicketForm()
        context= {'Form': form}
        return rener(request, 'ticket/create_ticket.html', context)
    
    #can see all created tickets
def customer_tickets(request):
    tickets = BaseTicket.objects.filter(customer = request.user)
    context= {'tickets':tickets}
    return render(request, 'ticket/customer_tickets.html', context)

# assign tickets to technicians

# Create your views here.