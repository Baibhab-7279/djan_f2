from django.shortcuts import redirect, render
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
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            userprofile = Profile.objects.get(username=username)
            print(userprofile.username)
            if(username == userprofile.username):
                userpassword = userprofile.password
                print(userpassword)
                if(password == userpassword):
                    semester = userprofile.semester
                    gender = userprofile.gender
                    email = userprofile.email
                    loginans = {
                        "ans": True,
                        "data": [semester,gender,email]
                    }
                    return render(request,"pages/page.html",loginans)
                
                else:
                    print("password incorrect")
            else:
                print("incorrect userprofile")
        except:
            print("not there")
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
        return render(request,"pages/page.html")
    return render(request,"pages/signup.html")