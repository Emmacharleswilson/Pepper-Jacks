from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
import datetime
from .models import Item, Table, Customer, Reservation
from .forms import CustomerForm, ReservationForm


# Create your views here.

class ReservationsEnquiry(View):
    def get(self, request, *args, **kwargs):
    
        customer_form = CustomerForm()
        reservation_form = ReservationForm()
    
        return render(request, "reservations.html",
            {'customer_form': customer_form,
            'reservation_form': reservation_form})


"""
def reservations(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'reservations.html', context)
"""