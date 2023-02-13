from django.shortcuts import render
from . form import Register

# Create your views here.

def register(request):
    form = Register()
    context = {
        "form":form
    }
    return render(request, "users/register.html", context)
