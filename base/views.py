from django.shortcuts import render
from .forms import customuser

# Create your views here.
def register(request, *args, **kwargs):
    form = customuser
    context = {
        'form':form
    }
    return render(request, "register.html", context)
