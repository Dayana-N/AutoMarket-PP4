from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/confirm', views.log_out_confirmation, name='logout-confirm'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/<str:pk>/', views.profile_page, name='profile'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('delete-profile/', views.delete_profile, name='delete-profile'),
    path('delete-profile/success/', views.delete_profile_success,
         name='delete-profile-success'),
]
