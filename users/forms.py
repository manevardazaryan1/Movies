from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# user app forms.py

# User register form class

class RegisterForm(UserCreationForm):
    """User register class"""

    class Meta:

        """User register class meta"""      

        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'password1', 'password2']
        help_texts = {
            'username': '',
            'last_name': '',
            'first_name': '',
            'email': '',
            'password1': '',
            'password2': '',
        }

# NEED TO REVIEW

# User update form class

class UserUpdateForm(UserChangeForm):
    """User update class"""

    class Meta:
        """User update meta class"""

        model = User
        fields = ['first_name', 'last_name', 'email']


# Profile update form class

class ProfileUpdateForm(forms.ModelForm):
    """Profile update class"""

    class Meta:

        """Profile meta class"""

        model = Profile
        fields = ['date_of_birth', 'phone_number']