from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('home')

        myuser = User.objects.create_user(username=username, password=password)
        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        if myuser is not None:
            login(request, myuser)
            # Redirect to the user-specific URL after signing up
            return redirect(reverse('user_home', args=[username]))

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the user-specific URL after signing in
            return redirect(reverse('user_home', args=[username]))
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

def user_home(request, username):
    # Ensure the logged-in user is the one accessing this page
    if request.user.is_authenticated and request.user.username == username:
        return render(request, "index.html", {'fname': username})
    else:
        messages.error(request, "You must be logged in to view this page.")
        return redirect('signin')
