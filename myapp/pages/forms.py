from django.db import models  
from django.forms import fields  
from .models import Userdata 
from django import forms  
  
  
class UserdataForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = Userdata
        # It includes all the fields of model  
        exclude = ("username","uploadtime")