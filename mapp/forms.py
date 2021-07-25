from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class MapInputs(forms.Form):
    latitude = forms.FloatField(label="Latitude", validators=[MinValueValidator(-55.99), MaxValueValidator(59.99)], initial=35.777789)
    longitude = forms.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)], label = 'Longitude', initial=-78.645747)
    scale = forms.FloatField(validators=[MinValueValidator(1), MaxValueValidator(4)], label = 'Map height (km)', initial=2.5)
    high_color = forms.CharField(max_length=36, label = 'Peak Color', initial="Red")
    low_color = forms.CharField(max_length=36, label = 'Valley Color', initial="Purple")
    x_dim = forms.IntegerField(validators=[MinValueValidator(4), MaxValueValidator(250)], label = 'Image Resolution: Width', initial=200)
    y_dim = forms.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(1000)], label = 'Image Resolution: Height', initial=200)
    dev_key = forms.CharField(max_length=40, label='Developer Key', initial="Paste your mapquest developer key here")
    # resolution = forms.IntegerField(validators=[MinValueValidator(4), MaxValueValidator(1024)], label = 'Image Resolution', initial=4)


