from django.shortcuts import render, redirect
from .models import BlogModel
from .forms import BlogModelForm,BlogUpdateForm


def home(request):
    blogs = BlogModel.objects.all()
    if request.method == "POST":
        form = BlogModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            return redirect("blog-index")
    else:
        form = BlogModelForm()
    context = {"blogs":blogs, "form":form}
    return render(request, "blog/index.html", context)


def post_detail(request, id):
    post = BlogModel.objects.get(id=id)
    context={
        "post":post
    }
    return render(request, "blog/detail.html", context)



def post_edit(request, id):
    post = BlogModel.objects.get(id=id)
    if request.method=="POST":
        form = BlogUpdateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog-detail", id=post.id)
    else:
        form = BlogUpdateForm(instance=post)
    context={
        "post":post,
        "form":form
    }
    return render(request,"blog/edit.html", context)