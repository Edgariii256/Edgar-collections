from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken..')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email exists')
                return redirect('login')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,)
                user.save();
                
                return redirect('/')
        else:
            messages.info(request,'Passwords do not match!!')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def reset_password(request):
    return render(request,'reset_password.html')