from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.validators import validate_email
# from customadmin.models import User
from django.urls import reverse


def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect("login")


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name  = request.POST['lastname']
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST['password']
        confirm_password = request.POST.get('confirm_password')
        if first_name.strip() == '' or last_name.strip() == ''or username.strip() == ''  or password.strip() == '' or confirm_password.strip() == '':
            messages.info(request,'fieild not empty')
            return redirect('signup') 
        email_check = validat_mail(email)
        if email_check is False:
            messages.info(request,'email not valid')
            return redirect('signup') 
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('signup')  
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('signup') 
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username, email=email, password=password)
                messages.success(request, 'Account created successfully. You can now log in.')
                return redirect('login')  
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')  
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')  
    else:
        if request.user.is_authenticated:
            return redirect("home")

        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def validat_mail(email):
    try:
        validate_email(email)
        return True
    except:
        return False
