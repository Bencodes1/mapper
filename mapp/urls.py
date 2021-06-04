# from .forms import MapInputs
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.homepage, name = 'homepage'),
    path('homepage/', views.homepage, name= 'homepage'),
    path('homepage/image/', views.image_render, name='image'),
]