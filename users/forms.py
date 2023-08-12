from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    """
    A class view handling registration form
    """
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }


class ProfileForm(ModelForm):
    """
    A class view handling creating and editing user profile
    """
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['created', 'user']
