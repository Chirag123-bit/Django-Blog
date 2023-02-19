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

    if request.method=="POST":
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None,  instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect("user-profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)



    context={
        "u_form":u_form,
        "p_form":p_form
    }
    return render(request, "users/profile.html",context)
