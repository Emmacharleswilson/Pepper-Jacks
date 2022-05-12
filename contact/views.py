from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


# Create your views here.
def homepage(request):
    """return home"""
    return render(request, "index.html")


def send_message(request, contact_form):
    """function to send email when message is submitted"""
    customer_fname = contact_form.cleaned_data['first_name']
    customer_lname = contact_form.cleaned_data['last_name']
    email_from = contact_form.cleaned_data['email_address']
    subject = (
        f'Message from {customer_fname}, {customer_lname}, {email_from}'
        )
    message = contact_form.cleaned_data['message']
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, email_from, recipient_list)


def contact(request):
    """funtion to validate and send alert when form is sent"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(request, form)

        messages.add_message(
                    request, messages.SUCCESS,
                    "Thank you, your message has been sent.")

    form = ContactForm()
    return render(request, "contact.html", {'form': form})
