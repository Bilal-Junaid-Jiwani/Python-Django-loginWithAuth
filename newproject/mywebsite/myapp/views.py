from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    if request.user.is_anonymous:
        return redirect("login")
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "✅ Login successful!")  # Message will now appear on index.html
            return redirect("home")  # Redirect to home page
        else:
            messages.error(request, "❌ Invalid username or password")
            return redirect("login")

    return render(request, "login.html")

def logoutuser(request):
    logout(request)
    messages.info(request, "ℹ️ You have been logged out.")
    return redirect("login")
