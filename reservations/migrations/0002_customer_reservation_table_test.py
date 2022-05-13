# Generated by Django 3.2 on 2022-05-04 17:38

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("customer_id", models.AutoField(primary_key=True, serialize=False)),
                ("full_name", models.CharField(max_length=50)),
                ("email", models.EmailField(default="", max_length=254)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, null=True, region=None
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Table",
            fields=[
                ("table_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "table_name",
                    models.CharField(default="New table", max_length=10, unique=True),
                ),
                ("max_no_people", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                ("test_id", models.AutoField(primary_key=True, serialize=False)),
                ("full_name", models.CharField(max_length=50)),
                ("full_done", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                ("reservation_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "no_of_guests",
                    models.IntegerField(
                        choices=[
                            (1, "1 person"),
                            (2, "2 people"),
                            (3, "3 people"),
                            (4, "4 people"),
                        ],
                        default=1,
                    ),
                ),
                ("requested_date", models.DateField()),
                (
                    "requested_time",
                    models.CharField(
                        choices=[
                            ("07:00", "07:00"),
                            ("08:00", "08:00"),
                            ("09:00", "09:00"),
                            ("10:00", "10:00"),
                            ("11:00", "11:00"),
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
                        ],
                        default="12:00",
                        max_length=10,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "pending"),
                            ("confirmed", "confirmed"),
                            ("rejected", "rejected"),
                            ("expired", "expired"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to="reservations.customer",
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="table_booked",
                        to="reservations.table",
                    ),
                ),
            ],
        ),
    ]
