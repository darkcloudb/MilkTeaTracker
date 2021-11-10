from django import forms
from django.forms.widgets import PasswordInput

# Create the form to create an account


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

# Create the Login Form


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=PasswordInput)



class EditProfileForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    prof_pic = forms.ImageField()