from django.shortcuts import render

# Create your views here.


def update_profile(request):
    '''
    A view that updates user's profile
    '''
    return render(request, 'users/update_profile.html')
