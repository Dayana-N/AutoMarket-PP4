from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import uuid


class CustomUserCreationForm(UserCreationForm):
    """
    A class handling registration form
    """
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }


class ProfileForm(forms.ModelForm):
    """
    A class view handling creating and editing user profile
    """
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['created', 'user']


class ContactForm(forms.Form):
    '''
    A class handling the contact form
    '''
    listing_id = forms.UUIDField(widget=forms.HiddenInput)
    listing = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
