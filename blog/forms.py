from django.forms import ModelForm
from .models import BlogModel

class BlogModelForm(ModelForm):
    class Meta:
        model = BlogModel
        fields = ("title", "content")
