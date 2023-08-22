from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Listing, CarMake
from . import choices
from .forms import ListingForm

# Create your views here.


def home_page(request):
    '''
    A view that displays the homepage
    '''
    listings = Listing.objects.all().order_by('-created')
    context = {
        'listings': listings,
    }
    return render(request, 'listings/index.html', context)


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
            messages.success(request, 'You listing has been created!')
            return redirect('single-listing', listing.pk)
        else:
            messages.error(request, 'Something went wrong! Please try again.')
    context = {
        'form': form,
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
        return redirect('profile', pk=profile.id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/delete_listing.html', context)


def load_models(request, pk):
    '''
    A view that returns car models in JSON format
    '''
    try:
        car_make = CarMake.objects.get(pk=pk)
        car_models = car_make.carmodel_set.all()
        data = [{model.id: model.name} for model in car_models]
        return JsonResponse(data, safe=False)
    except CarMake.DoesNotExist:
        return JsonResponse([], safe=False)


def single_listing(request, pk):
    '''
    A view that renders single listing
    '''
    listing = Listing.objects.get(pk=pk)
    context = {
        'listing': listing
    }
    return render(request, 'listings/single-listing.html', context)
