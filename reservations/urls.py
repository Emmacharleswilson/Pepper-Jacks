from django.urls import path, include
from reservations import views

urlpatterns = [
    path('', views.reservations, name='reservations'),
]
