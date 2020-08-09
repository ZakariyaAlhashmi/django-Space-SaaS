from django.shortcuts import render , redirect
from .forms import signupform, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profiles
from django.urls import reverse

# Create your views here.

def signup(request):
    if request.method =='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
            
    else:
        form = signupform()
    
    return render(request,'registration/signup.html',{'form':form} )

def profile(request):
    profile = Profiles.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})



def profile_edit(request):
    profile = Profiles.objects.get(user=request.user)

    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES , instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            theprofile = profileform.save(commit=False)
            theprofile.user = request.user
            theprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
 
    
    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})