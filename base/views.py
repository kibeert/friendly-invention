from django.shortcuts import render, redirect
from .forms import  customuser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def register(request, *args, **kwargs):
    form = customuser
    if request.method == "POST":
        form = customuser(request.POST)
        if form.is_valid():
            User = form.save(commit=False)
            User.username = User.username.lower()
            User.save()
            login(request, User)
            return redirect("home")
        return redirect("home")
    context = {
        'form':form
    }
    return render(request, "register.html", context)
