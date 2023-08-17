from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Listing
from . import choices
from .forms import ListingForm

# Create your views here.


def home_page(request):
    '''
    A view that displays the homepage
    '''
    return render(request, 'listings/index.html')


def listings(request):
    '''
    A view that displays the listings page
    '''
    listings = Listing.objects.all().order_by('-created')
    context = {
        'counties': choices.COUNTIES,
        'body_type': choices.BODY_TYPE,
        'fuel_type': choices.FUEL_TYPE,
        'transmission': choices.TRANSMISSION,
        'years': choices.get_year_choices(),
        'listings': listings
    }

    return render(request, 'listings/listings.html', context)


@login_required(login_url='login')
def create_listing(request):
    '''
    A view that handles creation of listings
    '''
    form = ListingForm()

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user.profile
            listing.save()

        return redirect('listings')

    context = {
        'form': form,
    }
    return render(request, 'listings/create_listing.html', context)
