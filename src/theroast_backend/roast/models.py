from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Roast(models.Model):
    # Name of the roast
    name = models.CharField(max_length=120)

    # Scale of 1-100 of how dark / light the roast is
    color = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                default=0)
