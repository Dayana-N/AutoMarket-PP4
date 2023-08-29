from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('listings/', views.listings, name='search-listings'),
    path('listings/<str:pk>/', views.single_listing, name='single-listing'),
    path('create-listing/', views.create_listing, name='create-listing'),
    path('delete-listing/<str:pk>/', views.delete_listing,
         name='delete-listing'),
    path('edit-listing/<str:pk>/', views.edit_listing,
         name='edit-listing'),
    path('favourite-listings/<str:pk>/', views.favourite_listings,
         name='favourite-listings'),
    path('remove-myfavourites/<str:pk>/', views.remove_myfavourites,
         name='remove-myfavourites'),
]
