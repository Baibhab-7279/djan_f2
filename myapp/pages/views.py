from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Page,Contactform,Profile



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
        cont = Contactform(yourname=yourname,email=email,subject=subject,message=message)
        cont.save()
    return render(request, "pages/contact.html")

def login(request):
    return render(request,"pages/login.html")

def signup(request):
    if(request.method == 'POST'):
        username = request.POST["username"]
        gender = request.POST["gender"]
        semester = request.POST["semester"]
        email = request.POST["email"]
        password = request.POST["password"]
        prof = Profile(username=username, gender=gender, semester=semester, email=email,password=password)
        prof.save()
    return render(request,"pages/signup.html")