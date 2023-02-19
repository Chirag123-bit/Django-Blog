from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class Register(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["email","username", "password1", "password2"]



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
    
        for fieldName in ["username", "email"]:
            self.fields[fieldName].help_text = None

    


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=["image"]