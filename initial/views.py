

from tabnanny import check
from unicodedata import name
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Commodities,Shop
from django.contrib import auth
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    goods=Commodities.objects.all()
    

    return render(request,'index.html',{'goods':goods})

def index0(request):
    kiosks=Shop.objects.all()

    return render(request,'index.html',{'kiosks':kiosks})


#def check_email_verification(user):
    return EmailVerification.objects.all().filter(user=user,verified=True)

#def check_email(function=None,redirect_field_name=REDIRECT_FIELD_NAME,login_url=None):
    actual_decorator=user_passes_test(check_email_verification,login_url=login_url,redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator


#@login_required
#@check_email(login_url="/redirect/login/?reason=verify_email")

