from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page or another appropriate view
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register_user.html', {'form': form})
