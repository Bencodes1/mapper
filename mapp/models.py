from django.db import models

# Create your models here.

class Map(models.Model):
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    scale = models.DecimalField(max_digits=4, decimal_places=2)
    high_color = models.CharField(max_length=36)
    low_color = models.CharField(max_length=36)
    resolution = models.IntegerField()

    def __str__(self):
        return self.high_color