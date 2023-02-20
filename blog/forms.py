from django.forms import ModelForm
from .models import BlogModel
from django import forms

class BlogModelForm(ModelForm):
    class Meta:
        model = BlogModel
        fields = ("title", "content")






class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields = ["title", "content"]
