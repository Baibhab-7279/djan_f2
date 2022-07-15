from unicodedata import name
from django.urls import path
from . import views

#url pattern here
urlpatterns = [
    path('', views.home, name="home"),
    path('services', views.services, name='services'),
    path('contact', views.contact, name="contact"),
]
