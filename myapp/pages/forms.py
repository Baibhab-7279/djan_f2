from django.db import models  
from django.forms import fields  
from .models import Userdata,Profile
from django import forms  
  
  
class UserdataForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = Userdata
        # It includes all the fields of model  
        exclude = ("username","uploadtime","imagename")

    def __init__(self, *args, **kwargs):
        super(UserdataForm, self).__init__(*args, **kwargs)
        self.fields['blogtext'].label = ""
        self.fields['blogtext'].widget = forms.Textarea(attrs={'placeholder': 'enter your blog here'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("profileimagename",)
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['email'].label = ""
        #self.fields['password'].label = ""

        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'username',"class":"profile"})
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder': '.....@gmail.com',"class":"profile"})
        

