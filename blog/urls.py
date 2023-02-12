from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="blog-index"),
   path("about/", views.about)
]
