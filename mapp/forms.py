from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class MapInputs(forms.Form):
    latitude = forms.FloatField(label="Latitude", validators=[MinValueValidator(-180), MaxValueValidator(180)], initial=41.40917)
    longitude = forms.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)], label = 'Longitude', initial=-122.19579)
    scale = forms.FloatField(validators=[MinValueValidator(1), MaxValueValidator(1000)], label = 'Map height (km)', initial=20.48)
    high_color = forms.CharField(max_length=36, label = 'Peak Color', initial="Red")
    low_color = forms.CharField(max_length=36, label = 'Valley Color', initial="Purple")
    x_dim = forms.IntegerField(validators=[MinValueValidator(4), MaxValueValidator(1999)], label = 'Image Resolution: Width', initial=1000)
    y_dim = forms.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(1999)], label = 'Image Resolution: Height', initial=48)
    # resolution = forms.IntegerField(validators=[MinValueValidator(4), MaxValueValidator(1024)], label = 'Image Resolution', initial=4)