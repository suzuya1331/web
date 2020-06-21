# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm,Subscribe
from core.settings import EMAIL_HOST_USER

from django.core.mail import send_mail,EmailMessage

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
def mail(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST,request.FILES)
        if sub.is_valid():
           
            subject = sub.cleaned_data.get('subject')
            message = sub.cleaned_data.get('body')
            recepient = sub.cleaned_data.get('Email')
            
            
            email = EmailMessage( subject, message, EMAIL_HOST_USER, [recepient])
            
            email.send()
           
            # send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            
            
            return render(request, './Success.html', {'recepient': recepient})
    return render(request, './mail.html', {'form':sub})
    