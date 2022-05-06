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


    def post(self, request, User=User, *args, **kwargs):
        # Get post data from forms
        customer_form = CustomerForm(data=request.POST)
        reservation_form = ReservationForm(data=request.POST)

        if customer_form.is_valid() and reservation_form.is_valid():
            # Retrieve information from forms
            customer_requested_date = request.POST.get('requested_date')
            customer_requested_time = request.POST.get('requested_time')
            customer_requested_guests = request.POST.get('no_of_guests')
            customer_name = request.POST.get('full_name')

             # Convert date into format required by django
            date_formatted = datetime.datetime.strptime(
                customer_requested_date, "%d/%m/%Y").strftime('%Y-%m-%d')

            customer_email = request.POST.get('email')
            # See if customer already exists in model
            customer_query = len(Customer.objects.filter(
                    email=customer_email))

            # Prevent duplicate 'customers' being added to database
            if customer_query > 0:
                pass
            else:
                customer_form.save()

            # Retreive customer information to pass to reservation model
            current_customer = Customer.objects.get(
                email=customer_email)
            current_customer_id = current_customer.pk
            customer = Customer.objects.get(
                customer_id=current_customer_id)

            reservation = reservation_form.save(commit=False)
            # Pass formatted date & customer in to model
            reservation.requested_date = date_formatted
            reservation.customer = customer
            # Save reservation
            reservation_form.save()

            messages.add_message(
                    request, messages.SUCCESS,
                    f"Thank you {customer_name}, your enquiry for "
                    f"{customer_requested_guests} people at "
                    f"{customer_requested_time} on "
                    f"{customer_requested_date} has been sent.")

            # Return blank forms so the same enquiry isn't sent twice.
            url = reverse('reservations')
            return HttpResponseRedirect(url)

        else:
            messages.add_message(
                request, messages.ERROR,
                "Something is not right with your form "
                "- please make sure your email address & phone number in the"
                " correct format.")

        return render(request, 'reservations.html',
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