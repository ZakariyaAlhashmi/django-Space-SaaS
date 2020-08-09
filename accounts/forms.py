# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profiles


class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1','password2' ]



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['city','phone_number','image']





    
