from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["Address"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirmPassword"]
        myUser = User.objects.create_user(username, email, password)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.save()
        return HttpResponseRedirect("/auth/signin")
    return render(request, "authentication/signup.html")


def signIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("user:--------------------------", user)
            fname = user.first_name
            return render(request, "authentication/index.html", {"fname": fname})
        else:
            messages.error(request, "bad credentials")
            redirect("home")
    return render(request, "authentication/signIn.html")


def signout(request):
    logout(request)
    return HttpResponseRedirect("/auth")
