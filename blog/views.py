from django.shortcuts import render, redirect
from .models import BlogModel
from .forms import BlogModelForm


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
