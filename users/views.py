from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm


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
            return redirect('home')
        else:
            messages.error(request, 'An error has occurred. Try again.')

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='login')
def profile_page(request):
    '''
    A view that renders user's profile
    '''
    profile = request.user.profile
    context = {
        'profile': profile
    }
    return render(request, 'users/profile_page.html', context)


def update_profile(request):
    '''
    A view that updates user's profile
    '''
    return render(request, 'users/update_profile.html')
