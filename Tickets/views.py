from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
import random, string

def ticket_home(request):
    return render(request,'hello.html')