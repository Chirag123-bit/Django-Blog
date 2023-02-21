from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="blog-index"),
   path("post/<int:id>/", views.post_detail, name="blog-detail"),
   path("edit/<int:id>/", views.post_edit, name="blog-edit"),
   path("delete/<int:id>/", views.post_delete, name="blog-delete"),
]
