from re import sub
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Page,Contactform



# Create your views here.
def home(request):
    pg = Page.objects.get(id = 1)
    context = {
        "obj": pg,
        "page_list": Page.objects.all()
    }
    return render(request, 'pages/page.html', context)

def services(request):
    return render(request, 'pages/page_1.html')

def contact(request):
    if(request.method == 'POST'):
        yourname = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        print(name,email,subject,message)
        cont = Contactform(yourname=yourname,email=email,subject=subject,message=message)
        cont.save()
    return render(request, "pages/contact.html")
