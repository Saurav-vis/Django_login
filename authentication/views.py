from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from OPdjango import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail.message import EmailMessage
from . tokens import generate_token

# Create your views here.
# from werkzeug.utils import redirect


def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request,"Email already registered")
            return redirect('home')

        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")

        if password != confirmpassword:
            messages.error(request,"Password Don't matched")

        if not username.isalnum():
            messages.error(request,"Username must be Alpha-Numeric!")
            return redirect('home')

        myuser = User.objects.create_user(username,email,password)
        myuser.firstname = firstname
        myuser.lastname = lastname
        myuser.is_active = True

        myuser.save()

        messages.success(request, "Your account has been successfully created. ")



        return redirect('signin')

    return render(request,"authentication/signup.html")



def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            # firstname = user.firstname
            messages.success(request, "You have successfully Logged in.")
            return render(request, "authentication/index.html")

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect('home')



def update(request):
    return render(request, 'reset-password.html')