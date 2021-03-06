from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

import uuid

USER_MODEL = get_user_model()

class RoastImage(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    path = models.CharField(max_length=200)
    position = models.IntegerField(default=0)

class Roast(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    long_description = models.CharField(max_length=800)
    short_description = models.CharField(max_length=120)

    # Scale of 1-100 of how dark / light the roast is
    color = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                default=0)

    # Indicates if the coffee information will be shown
    # since it must be approved.
    ready = models.BooleanField(default=False)
    images = models.ManyToManyField(RoastImage)

class ContactInfo(models.Model):
    """
    We make this a database model since
    a company, shop, and roastery may have a
    common contact info. These values
    will all be unique.

    email
    phone number

    maybe more

    """
    pass

class Company(models.Model):
    """
    Parent object to a collection of shops
    and a collection of roasterys. As many
    coffee shops will serve other roasts, but 
    then expand into roasting as well.
    """
    owner = models.ForeignKey(USER_MODEL, related_name='company_owner', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=240)
    roasterys = models.ForeignKey('Roastery', related_name='roasteries', null=True, on_delete=models.SET_NULL)
    shops = models.ForeignKey('Shop', related_name='shops', null=True, on_delete=models.SET_NULL)

class Shop(models.Model):
    """
    Represents a physical coffee shop.
    """
    owner = models.ForeignKey(USER_MODEL, related_name='shop_owner', null=True, on_delete=models.SET_NULL)
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
    owner = models.ForeignKey(USER_MODEL, related_name='roastery_owner', null=True, on_delete=models.SET_NULL)
    roasts = models.ForeignKey('Roast', related_name='roastery_roasts', on_delete=models.CASCADE)

    """
    location.. (maybe)
    contact info (foreign key)
    user who owns the roastery
        *can be unclaimed (null)
    """

