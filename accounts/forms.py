# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    USER_TYPES = (
        ('tech', 'Tech'),
        ('staff', 'Staff'),
        ('admin', 'Admin')
    )

    user_type = forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password1', 'password2', 'user_type', 'location']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = self.cleaned_data['user_type']

        if user.user_type == 'admin':
            user.is_staff = True
            user.is_superuser = True

        if commit:
            user.save()

        return user
