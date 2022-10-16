
from django.shortcuts import render,redirect
from  .models import *
from .backends import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.



def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=make_password(request.POST.get('psw'))
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        try:
            myuser=Myuser.objects.create( username=fname,email=email,password=password,first_name=fname,last_name=lname,address=address)
            return redirect('user_login')
        except:
            pass
    return render(request,'register.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('psw')
        user=EmailBackend.authenticate(request,username=username,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect('profile')
    return render(request,'login.html')

def signout(request):
    logout(request)
    return redirect('user_login')      

def profile(request):
    user=request.user
    context={'user':user}
    return render(request,'profile.html',context)    


def profile_edit(request):
    id=request.GET.get('id')
    try:
        user=Myuser.objects.get(id=id)
    except:
        return redirect('profile')    
    context={'user':user}
    if request.method=='POST':
        if request.POST.get('email'):
            user.email=request.POST.get('email')
        if request.POST.get('fname'):
            user.first_name=request.POST.get('fname')
        if request.POST.get('lname'):
            user.last_name=request.POST.get('lname')
        if request.POST.get('address'):
            user.address=request.POST.get('address')
        if request.POST.get('mobile_number'):
            user.mobile_number=request.POST.get('mobile_number') 
        if request.POST.get('age'):
            user.age=request.POST.get('age')
        if request.POST.get('profile_pic'):
            user.profile_pic=request.Files.get('profile_pic')   
        user.save() 
        return redirect('profile')
    return render(request,'profile_edit.html',context)                           

