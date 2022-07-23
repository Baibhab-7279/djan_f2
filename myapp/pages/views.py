from distutils.command.build_scripts import first_line_re
from email.errors import MalformedHeaderDefect
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Page,Contactform,Profile



username = "Baibhab@7279"
password = "Baibhab@7279"
ans = False
gender = "male"
semester = "first"
email = "mrbaibhab5816@gmail.com"

# Create your views here.
def home(request):
    pg = Page.objects.get(id = 1)
    context = {
        "obj": pg,
        "page_list": Page.objects.all()
    }
    return render(request, 'pages/home.html',check())

def aboutus(request):
    return render(request, 'pages/aboutus.html',check())

def contact(request):
    if(request.method == 'POST'):
        yourname = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        cont = Contactform(yourname=yourname,email=email,subject=subject,message=message)
        cont.save()
    
    return render(request, "pages/contact.html",check())

def login(request):
    global username,gender,semester,email,ans
    ans = False
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
                    ans = True
                    
                    return render(request,"base.html",check())
                
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

def logout(request):
    global ans
    ans = False
    return render(request,"base.html",check())



def check():
    loginans = {
        "ans": ans,
        "username": username,
        "gender": gender,
        "semester": semester,
        "email": email,
    }
    return loginans
