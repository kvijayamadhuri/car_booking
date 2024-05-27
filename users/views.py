from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import User

def register_user(request):
   if request.method=="POST":
      uname=request.POST["user_name"]
      email=request.POST["user_email"]
      password_one=request.POST["user_password_one"]
      password_two=request.POST["user_password_two"]
   
      if password_one==password_two:
         if User.objects.filter(username=uname).exists():
            messages.warning(request, f'user name is there {uname} take alternatine one')
            return redirect ('/users/register-user/')
         else:
            User.objects.create_user(username=uname, email=email, password=password_one)
            messages.success(request, 'user is registerd successfully')
            return redirect('/users/login-user/')
      else:
         messages.warning('password and confirm password not matched')
         return redirect ("/users/register-user/")
   return render (request,'users/register_user.html')


def login_user(request):
   if request.method=="POST":
      uname = request.POST["user_name"]
      password = request.POST["user_password"]
      user = authenticate(username=uname, password=password)
      if user is not None:
         login(request, user)
         return redirect("/")
   return render(request, 'users/login_user.html')

def logout_user(request):
    logout(request)
    return redirect("/")