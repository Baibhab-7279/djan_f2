import os
from django.conf import settings
from .forms import ProfileForm,UserdataForm
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Page, Contactform, Profile, Title,UserData


username = "Baibhab@7279"
password = "Baibhab@7279"
title = "post it"
ans = False
gender = "male"
semester = "first"
email = "mrbaibhab5816@gmail.com"
profileimage = "maleprofile.png"


# Create your views here.
def home(request):
    # path = settings.MEDIA_ROOT
    # img_list = os.listdir(path + '/images')

    ch = check()

    global title
    title1 = Title.objects.last()
    print(title)
    if(title1):
        ch["title"] = title1

    else:
        ch["title"] = title

    # ch["images"] = img_list

    print(ch)

    a = UserData.objects.filter(choise="public").values("image", "blogtext","email")
    print(a)
    c = []
    d = []
    for i in range(len(a)-1,-1,-1):
        b = a[i]
        print(b)
        c.append(b["image"])
        # print(c)
        e = b["blogtext"]

        f = b["email"]
        g = f.split("@")
        h = f"{g[0]}.jpg"

        c.append(e)
        c.append(h)
        d.append(c)
        # print(d)
        c = []
        # c.append(b["image"])
        # d.append(b["blogtext"])
    print(c)
    print(d)
    ch = check()
    # ch["images"] = c
    ch["content"] = d

    if(ans == True):
        a1 = UserData.objects.filter(choise="private").values("image", "blogtext","email")
        print(a)
        for i in range(len(a1)):
            b1 = a1[i]
            print(b1)
            c.append(b1["image"])
            # print(c)
            e1 = b1["blogtext"]

            f = b1["email"]
            g = f.split("@")
            h = f"{g[0]}.jpg"

            c.append(e1)
            c.append(h)
            d.append(c)
            # print(d)
            c = []
            # c.append(b["image"])
            # d.append(b["blogtext"])
        print(c)
        print(d)
        ch = check()
        # ch["images"] = c
        ch["content"] = d

        return render(request, 'pages/home.html', ch)
    print("we are here")
    return render(request, 'pages/home.html', ch)


def aboutus(request):
    return render(request, 'pages/aboutus.html', check())


def contact(request):
    if(request.method == 'POST'):
        yourname = request.POST["name_co"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        cont = Contactform(yourname=yourname, email=email,subject=subject, message=message)
        cont.save()

    return render(request, "pages/contact.html", check())


def login(request):

    if(request.method == "POST"):
        

        username1 = request.POST["username"]
        password1 = request.POST["password"]
        try:
            global profileimage, username, gender, semester, email, ans
            userprofile = Profile.objects.get(username=username1)
            print(userprofile.username)
            if(username1 == userprofile.username):
                userpassword = userprofile.password
                print(userpassword)
                if(password1 == userpassword):
                    ans = True
                    username = userprofile.username 
                    semester = userprofile.semester
                    gender = userprofile.gender
                    email = userprofile.email
                    profileimage = userprofile.profileimagename

                    check()

                    return redirect("/")

                else:
                    print("password incorrect")
            else:
                print("incorrect userprofile")
        except:
            print("not there")
    return render(request, "pages/login.html")


def signup(request):

    print("we are here")
    if(request.method == 'POST'):

        print("we are here 1")
        profileform = ProfileForm(request.POST, request.FILES)
        print("we are here 3")

        if(profileform.is_valid()):
            profileauth = profileform.save(commit=False)
            profimg = profileauth.email
            profimg1 = profimg.split("@")
            profileauth.profileimage.name = f"{profimg1[0]}.jpg"
            profileauth.profileimagename = profileauth.profileimage.name
            profileauth.save()
            print(profileauth.profileimage.name)

            global profileimage, username, gender, semester, email, ans
            print(profileimage, username, gender, semester, email)

            ans = True
            gender = profileauth.gender
            semester = profileauth.semester
            username = profileauth.username
            email = profileauth.email
            profileimage = profileauth.profileimagename

            print(profileimage, username, gender, semester, email)

            profilecheck1 = check()

            # print(profileimage)
            # profilecheck["ans"] = True
            # profilecheck["profileimage"] = profileauth.profileimagename
            # print(profilecheck["profileimage"])
            # profilecheck["profileform"] = profileform
            print(profilecheck1)
            return render(request, "base.html", profilecheck1)
        else:
            print("we are on the else page")
            profileform = ProfileForm()
            profilecheck = check()
            profilecheck["profileform"] = profileform
            print(profilecheck)
            print("we are here 2")
            profilecheck["alertmessage"] = "this email id has been taken"
            return render(request, "pages/signup.html", profilecheck)
    else:
        print("we are on the else page")
        profileform = ProfileForm()
        profilecheck = check()
        profilecheck["profileform"] = profileform
        print(profilecheck)
        return render(request, "pages/signup.html", profilecheck)

    return render(request, "pages/signup.html", profilecheck)


def logout(request):
    global ans
    ans = False
    return redirect("/")


def upload(request):
    pas1 = check()
    if(ans == True):
        if request.method == 'POST':
            form = UserdataForm(request.POST, request.FILES)
            if form.is_valid():
                global username,email
                # a = Userdata.objects.get(username = username)
                newauth = form.save(commit=False)
                newauth.username = username
                newauth.imagename = newauth.image.name
                newauth.email = email
                newauth.save()
                # print(a.image.name)
                print(newauth.image.name)
                a = UserData.objects.filter(username='baibhab kumar pradhan').values()
                print(a)

                # Getting the current instance object to display in the template
                img_object = form.instance

                details = check()
                details["form"] = form
                details["img_obj"] = img_object
                details["alertmessage"] = "succefully uploaded"
                return render(request, 'pages/upload.html', details)
        else:
            form = UserdataForm()
            pas = check()
            pas["form"] = form
    else:
        return render(request, "pages/unupload.html", pas1)

    return render(request, "pages/upload.html", pas)


def check():
    loginans = {
        "ans": ans,
        "title": title,
        "username": username,
        "gender": gender,
        "semester": semester,
        "email": email,
        "profileimage": profileimage
    }
    return loginans
