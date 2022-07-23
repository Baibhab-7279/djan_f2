from unicodedata import name
from django.urls import path
from . import views

#url pattern here
urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact', views.contact, name="contact"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
]
