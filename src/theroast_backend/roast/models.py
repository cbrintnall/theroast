from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Roast(models.Model):
    # Name of the roast
    name = models.CharField(max_length=120)

    # Scale of 1-100 of how dark / light the roast is
    color = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                default=0)

class Company(models.Model):
    """
    Parent object to a collection of shops
    and a collection of roasterys. As many
    coffee shops will serve other roasts, but 
    then expand into roasting as well.
    """
    name = models.CharField(max_length=240)
    roasterys = models.ForeignKey('Roastery', related_name='roasteries', null=True, on_delete=models.SET_NULL)
    shops = models.ForeignKey('Shop', related_name='shops', null=True, on_delete=models.SET_NULL)

class Shop(models.Model):
    """
    Represents a physical coffee shop.
    """
    serves_food = models.BooleanField()
    has_seating = models.BooleanField()
    roasts = models.ManyToManyField('Roast', related_name='shop_roasts')


    """
    location.. (maybe)
    """

class Roastery(models.Model):
    """
    Represents a physical roastery.
    """
    roasts = models.ForeignKey('Roast', related_name='roastery_roasts', on_delete=models.CASCADE)

    """
    location.. (maybe)
    contact info (foreign key)
    user who owns the roastery
        *can be unclaimed (null)
    """

