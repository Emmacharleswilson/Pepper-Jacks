from django.db import models

# Create your models here.


class FoodItem(models.Model):
    """
    Food items model
    """
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    allergens = models.CharField(max_length=200, null=True)
    on_menu = models.BooleanField(default=True)

    class Meta:
        ordering = ['-on_menu']

    def __str__(self):
        return self.dish_name


class DrinkItem(models.Model):
    """
    Drink items model
    """
    drink_id = models.AutoField(primary_key=True)
    drink_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    allergens = models.CharField(max_length=200, null=True)
    on_menu = models.BooleanField(default=False)

    class Meta:
        ordering = ['-on_menu']

    def __str__(self):
        return self
