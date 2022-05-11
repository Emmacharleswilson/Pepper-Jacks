from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


status_choices = (("pending", "pending"),
                  ("confirmed", "confirmed"),
                  ("rejected", "rejected"),
                  ("expired", "expired"))


time_choices = (
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
    ("21:00", "21:00"),
    ("22:00", "22:00"),
    )


guests_choices = ((1, "1 person"),
                  (2, "2 people"),
                  (3, "3 people"),
                  (4, "4 people"),
                  (5, "5 people"),
                  (6, "6 people"),)


# Create your models here
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, default="")
    phone_number = PhoneNumberField(null=True)

    def __str__(self):
        # return the full name as this is easier for the admin to read
        return self.full_name


class Table(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(
        max_length=10, default="New table", unique=True)
    max_no_people = models.IntegerField()

    def __str__(self):
        return self.table_name


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer", null=True)
    no_of_guests = models.IntegerField(choices=guests_choices, default=1)
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=10, choices=time_choices, default='12:00')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="table_booked", null=True)
    status = models.CharField(
        max_length=10, choices=status_choices, default="pending")

    def __str__(self):
        return str(self.reservation_id)
