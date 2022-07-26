
from .forms import UserdataForm
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Page,Contactform,Profile,Userdata



username = "Baibhab@7279"
password = "Baibhab@7279"
ans = False
gender = "male"
semester = "first"
email = "mrbaibhab5816@gmail.com"

# Create your views here.
def home(request):
    return render(request, 'pages/home.html',check())

def aboutus(request):
    return render(request, 'pages/aboutus.html',check())

def contact(request):
    if(request.method == 'POST'):
        yourname = request.POST["name_co"]
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
                    
                    return redirect("/")
                
                else:
                    print("password incorrect")
            else:
                print("incorrect userprofile")
        except:
            print("not there")
    return render(request,"pages/login.html")

def signup(request):
    if(request.method == 'POST'):
        global ans,username,gender,email,semester
        ans = True

        username = request.POST["username"]
        gender = request.POST["gender"]
        semester = request.POST["semester"]
        email = request.POST["email"]
        password = request.POST["password"]
        prof = Profile(username=username, gender=gender, semester=semester, email=email,password=password)
        prof.save()

        return redirect("/")
    return render(request,"pages/signup.html")

def logout(request):
    global ans
    ans = False
    return redirect("/")

def upload(request):
    if request.method == 'POST':  
        form = UserdataForm(request.POST, request.FILES)
        if form.is_valid(): 
            global username 
            newauth = form.save(commit=False)  
            newauth.username = username
            newauth.save()


            # Getting the current instance object to display in the template  
            img_object = form.instance

            details = check()
            details["form"] = form 
            details["img_obj"] = img_object

              
            return render(request, 'pages/upload.html', details)  
    else:  
        form = UserdataForm()
        pas = check()
        pas["form"] = form 
    return render(request,"pages/upload.html",pas)




def check():
    loginans = {
        "ans": ans,
        "username": username,
        "gender": gender,
        "semester": semester,
        "email": email,
    }
    return loginans
