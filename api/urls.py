from django.urls import path
from . import views

urlpatterns = [
    path('car-model/<str:pk>/', views.getCarModel, name='get-carmodel'),
]
