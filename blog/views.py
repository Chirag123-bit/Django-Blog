from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogModel
from .forms import BlogModelForm


def home(request):
    blogs = BlogModel.objects.all()
    form = BlogModelForm()
    context = {"blogs":blogs, "form":form}
    return render(request, "blog/index.html", context)

def about(request):
    return HttpResponse("About Page")

