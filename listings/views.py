from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Listing, CarMake, CarModel
from . import choices
from .forms import ListingForm

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
        'listings': listings
    }
    return render(request, 'listings/index.html', context)


def search_listings(request):
    '''
    A view that handles the search functionality
    '''
    listings = Listing.objects.all().order_by('-created')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # get the keywords and split them
            keywords_list = keywords.split()
            keyword_query = Q()

            # for each word create a filter
            for keyword in keywords_list:
                keyword_query &= Q(description__icontains=keyword) | Q(
                    car_make__name__icontains=keyword) | Q(
                        car_model__name__icontains=keyword)

            listings = listings.filter(keyword_query)

    if 'town' in request.GET:
        town = request.GET['town']
        if town:
            listings = listings.filter(town__iexact=town)

    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            listings = listings.filter(county__iexact=county)

    if 'fuel' in request.GET:
        fuel = request.GET['fuel']
        if fuel:
            listings = listings.filter(fuel_type__iexact=fuel)

    if 'min_year' in request.GET:
        min_year = request.GET['min_year']
        if min_year:
            listings = listings.filter(year__gte=min_year)

    if 'max_year' in request.GET:
        max_year = request.GET['max_year']
        if max_year:
            listings = listings.filter(year__lte=max_year)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        if min_price:
            listings = listings.filter(price__gte=min_price)

    if 'max_price' in request.GET:
        max_price = request.GET['max_price']
        if max_price:
            listings = listings.filter(price__lte=max_price)

    # Pagination
    paginator = Paginator(listings, 2)
    page_number = request.GET.get("page")
    listings = paginator.get_page(page_number)
    context = {
        'counties': choices.COUNTIES,
        'body_type': choices.BODY_TYPE,
        'fuel_type': choices.FUEL_TYPE,
        'transmission': choices.TRANSMISSION,
        'years': choices.get_year_choices(),
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
            return redirect('single-listing', listing.pk)
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
        return redirect('profile', pk=profile.id)
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
            return redirect('single-listing', pk=listing.id)
        else:
            messages.error(request, 'Something went wrong! Please try again.')

    context = {
        'form': form,
        'page': page
    }
    return render(request, 'listings/listing_form.html', context)


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
