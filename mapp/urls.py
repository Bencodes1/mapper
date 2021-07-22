from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name= 'homepage'),
    path('homepage/image/', views.image_render, name='image'),
]