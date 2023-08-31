from .models import Listing
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .cars import cars
from .models import CarMake, CarModel


def search_listings(request):
    '''
    A function that handles the search functionality
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

    return listings


def listings_pagination(request, listings):
    '''
    A function that handles the pagination
    '''
    paginator = Paginator(listings, 6)
    page_number = request.GET.get("page")
    try:
        listings = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        listings = paginator.page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        listings = paginator.page(page_number)
    return listings, page_number


def load_data():
    '''
    load data to database
    '''
    for key, value in cars.items():
        car_make_instance, created = CarMake.objects.get_or_create(
            name=key)

        for item in value:
            CarModel.objects.create(name=item, car_make=car_make_instance)

    print('done')


# load_data()
