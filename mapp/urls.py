# from .forms import MapInputs
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('homepage2/', views.homepage2, name= 'homepage2'),
    path('image/', views.image_render, name='image'),
]