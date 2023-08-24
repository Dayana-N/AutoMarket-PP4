from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile
from .emails import contact_body
from listings.models import Listing
from smtplib import SMTPException
import os


# Create your views here.


def login_user(request):
    '''
    A view that handles login
    '''

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect login details')

    return render(request, 'users/login.html')


def log_out_confirmation(request):
    return render(request, 'users/logout-confirmation.html')


def logout_user(request):
    '''
    A view that handles user logout
    '''
    logout(request)
    messages.info(request, 'You have logged out')
    return redirect('home')


def register_user(request):
    '''
    A view that handles user registration
    '''
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have successfully registered')
            login(request, user)
            return redirect('update-profile')
        else:
            messages.error(request, 'An error has occurred. Try again.')

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='login')
def profile_page(request, pk):
    '''
    A view that renders user's profile
    '''
    profile = Profile.objects.get(id=pk)
    listings = profile.listing_set.all()
    context = {
        'profile': profile,
        'listings': listings
    }
    return render(request, 'users/profile_page.html', context)


def user_account(request, pk):
    '''
    A view that renders user's account page
    '''
    profile = Profile.objects.get(id=pk)
    listings = profile.listing_set.all()
    context = {
        'profile': profile,
        'listings': listings
    }
    return render(request, 'users/user_account.html', context)


@login_required(login_url='login')
def update_profile(request):
    '''
    A view that updates user's profile
    '''
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile', profile.id)
        else:
            messages.error(request, 'An error has occurred. Try again.')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'users/update_profile.html', context)


def delete_profile(request):
    '''
    A view that deletes user's profile
    '''
    if request.method == 'POST':
        user_profile = request.user.profile
        user_profile.delete()

        messages.success(request, 'Profile deleted successfully.')
        return redirect('delete-profile-success')
    return render(request, 'users/delete_profile.html')


def delete_profile_success(request):
    '''
    A view that displays delete warning to user
    '''
    return render(request, 'users/delete_profile_confirmation.html')


def contact(request, pk):
    if request.method == 'POST':
        listing_owner = get_object_or_404(Profile, id=pk)
        sender_email = request.POST.get('email')
        sender_phone = request.POST.get('phone')
        sender_name = request.POST.get('name')
        message = request.POST.get('message')
        listing_title = request.POST['listing']
        listing_id = request.POST.get('listing_id')
        current_listing = get_object_or_404(Listing, id=listing_id)

        print(listing_owner, sender_email, sender_phone)
        subject = f'New Message {current_listing.listing_title}'

        try:
            send_mail(
                subject,
                contact_body.format(
                    sender_name=sender_name, sender_email=sender_email,
                    message=message),
                os.environ.get('EMAIL_HOST_USER'),
                [sender_email],
                fail_silently=False,
            )

            messages.success(request, 'Email sent successfully!')
        except SMTPException as e:
            messages.error(
                request, 'An error has occurred sending this email.')

        return redirect('single-listing', current_listing.id)
