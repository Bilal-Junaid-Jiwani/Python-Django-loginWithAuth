from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login  # Fixed typo

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")

def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)  # Fixed typo

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})  # Show error message

    # Handle GET request by rendering the login page
    return render(request, "login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")
