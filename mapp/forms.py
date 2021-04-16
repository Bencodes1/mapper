from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class MapInputs(forms.Form):
    latitude = forms.DecimalField(label="Latitude", max_digits=8, decimal_places=5, initial=41.40917)
    longitude = forms.DecimalField(max_digits=8, decimal_places=5, label = 'Longitude', initial=-122.19579)
    scale = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Map radius (km)', initial=20.48)
    high_color = forms.CharField(max_length=36, label = 'Peak Color', initial="Red")
    low_color = forms.CharField(max_length=36, label = 'Valley Color', initial="Purple")
    resolution = forms.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(1024)], label = 'Image Resolution', initial=64)