from django.shortcuts import render, redirect
from . form import Register

# Create your views here.

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog-index")

    else:
        form = Register()

    context = {
        "form":form
    }
    return render(request, "users/register.html", context)


def profile(request):
    return render(request, "users/profile.html")
