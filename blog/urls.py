from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="blog-index"),
   path("post/<int:id>/", views.post_detail, name="blog-detail"),

]
