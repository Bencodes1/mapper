from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Map(models.Model):
    latitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    scale = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    high_color = models.CharField(max_length=36)
    low_color = models.CharField(max_length=36)
    resolution = models.IntegerField()

    def __str__(self):
        return self.high_color