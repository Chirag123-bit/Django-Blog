from django.shortcuts import render, redirect
from . form import Register,UserUpdateForm,ProfileUpdateForm


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
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user)

    context={
        "u_form":u_form,
        "p_form":p_form
    }
    return render(request, "users/profile.html",context)
