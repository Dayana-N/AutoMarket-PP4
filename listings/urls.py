from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('listings/', views.listings, name='listings'),
    path('listings/<str:pk>/', views.single_listing, name='single-listing'),
    path('create-listing/', views.create_listing, name='create-listing'),
    path('load-models/<str:pk>', views.load_models, name='load-models'),
]
