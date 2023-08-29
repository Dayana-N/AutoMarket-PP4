from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Listing, CarMake, CarModel, Favourite
from . import choices
from .forms import ListingForm
from .utils import search_listings, listings_pagination

# Create your views here.


def home_page(request):
    '''
    A view that displays the homepage
    '''
    listings = Listing.objects.all().order_by('-created')
    context = {
        'counties': choices.COUNTIES,
        'body_type': choices.BODY_TYPE,
        'fuel_type': choices.FUEL_TYPE,
        'transmission': choices.TRANSMISSION,
        'years': choices.get_year_choices(),
        'price_options': choices.PRICE_OPTIONS,
        'listings': listings
    }
    return render(request, 'listings/index.html', context)


def listings(request):
    '''
    A view that displays all listings and handles
    the search functionality and pagination
    '''
    listings = search_listings(request)
    listings, page_number = listings_pagination(request, listings)

    context = {
        'counties': choices.COUNTIES,
        'body_type': choices.BODY_TYPE,
        'fuel_type': choices.FUEL_TYPE,
        'transmission': choices.TRANSMISSION,
        'years': choices.get_year_choices(),
        'price_options': choices.PRICE_OPTIONS,
        'listings': listings,
        'values': request.GET
    }

    return render(request, 'listings/listings.html', context)


@login_required(login_url='login')
def create_listing(request):
    '''
    A view that handles creation of listings
    '''
    form = ListingForm()
    page = 'create'

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user.profile
            listing.save()
            messages.success(request, 'You listing has been created!')
            return redirect('my-listings', listing.owner.id)
        else:
            messages.error(request, 'Something went wrong! Please try again.')
    context = {
        'form': form,
        'page': page,
    }
    return render(request, 'listings/listing_form.html', context)


@login_required(login_url='login')
def delete_listing(request, pk):
    '''
    A view that handles deleting listings
    '''
    listing = get_object_or_404(Listing, pk=pk)
    profile = request.user.profile

    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'Listing deleted successfully.')
        return redirect('my-listings', pk=profile.id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/delete_listing.html', context)


@login_required(login_url='login')
def edit_listing(request, pk):
    '''
    A view that handles edit listings
    '''
    page = 'edit'
    profile = request.user.profile
    listing = profile.listing_set.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            listing = form.save()
            messages.success(request, 'Listing updated successfully.')
            return redirect('my-listings', profile.id)
        else:
            messages.error(request, 'Something went wrong! Please try again.')

    context = {
        'form': form,
        'page': page
    }
    return render(request, 'listings/listing_form.html', context)


def single_listing(request, pk):
    '''
    A view that renders single listing
    '''
    listing = Listing.objects.get(pk=pk)
    favourite = bool

    if request.user.is_authenticated:
        profile = request.user.profile.id
        if Favourite.objects.filter(owner=profile, listing=listing).exists():
            favourite = True

    context = {
        'listing': listing,
        'favourite': favourite
    }
    return render(request, 'listings/single-listing.html', context)


@login_required(login_url='login')
def favourite_listings(request, pk):
    '''
    A view that adds and removes listings from favourites
    on profile page
    '''
    listing = get_object_or_404(Listing, pk=pk)
    profile = request.user.profile
    favourite_listing, created = Favourite.objects.get_or_create(
        owner=profile, listing=listing)

    if created:
        messages.success(request, 'Listing saved.')
    else:
        favourite_listing.delete()
        messages.success(request, 'Listing removed.')

    return redirect('single-listing', pk=pk)


@login_required(login_url='login')
def remove_myfavourites(request, pk):
    '''
    A view that removes listing from favourites on profile page
    '''
    listing = get_object_or_404(Listing, pk=pk)
    profile = request.user.profile

    if request.method == 'POST':
        favourite_listing = get_object_or_404(
            Favourite, owner=profile, listing=listing)
        if favourite_listing:
            favourite_listing.delete()
            messages.success(request, 'Listing removed.')
            return redirect('my-favourites', pk=profile.id)

    context = {
        'listing': listing
    }
    return render(
        request, 'listings/delete_favourite_confirmation.html', context)
