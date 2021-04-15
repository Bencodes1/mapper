from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class MapInputs(models.Model):
    latitude = models.DecimalField(max_digits=8, decimal_places=5, initial=41.40917)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, initial=-122.19579)
    scale = models.DecimalField(max_digits=4, decimal_places=2, initial=20)
    high_color = models.CharField(max_length=36, initial="Red")
    low_color = models.CharField(max_length=36, initial="Purple")
    resolution = models.IntegerField(validators=[MinValueValidator(16),
                                       MaxValueValidator(1024)], initial=1024)