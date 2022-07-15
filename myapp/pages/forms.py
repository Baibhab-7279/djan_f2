from django import forms

class contactform(forms.Form):
    yourname = forms.CharField(max_length=100,label="your name")
    email = forms.EmailField(required=False, label="your email address")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)