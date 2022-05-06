from django.urls import path, include
from reservations import views


urlpatterns = [
    path('', views.ReservationsEnquiry.as_view(), name='reservations'),
]
