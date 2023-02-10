from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogModel


def home(request):
    blogs = BlogModel.objects.all()
    return render(request, "blog/index.html", {"blogs":blogs})

def about(request):
    return HttpResponse("About Page")

