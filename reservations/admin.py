from django.contrib import admin
from .models import Item, Customer, Table, Reservation


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'done')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'full_name', 'email', 'phone_number')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_name', 'max_no_people')


@admin.register(Reservation)
class ReservationsAdmin(admin.ModelAdmin):
    list_filter = ('no_of_guests', 'status', 'table_id')
    list_display = ('reservation_id', 'customer', 'no_of_guests', 'status',
                    'table', 'requested_date', 'requested_time')
