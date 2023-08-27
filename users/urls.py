from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/confirm', views.log_out_confirmation, name='logout-confirm'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/<str:pk>/my-profile/', views.profile_page, name='profile'),
    path('profile/<str:pk>/my-listings/',
         views.profile_listings, name='my-listings'),
    path('profile/<str:pk>/my-favourites/',
         views.profile_favourites, name='my-favourites'),
    path('user-account/<str:pk>/', views.user_account, name='user-account'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('delete-profile/', views.delete_profile, name='delete-profile'),
    path('delete-profile/success/', views.delete_profile_success,
         name='delete-profile-success'),
    path('contact/<str:pk>/', views.contact, name='contact'),
]
