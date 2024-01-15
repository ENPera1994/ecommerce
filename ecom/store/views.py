from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User




def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})


def about(request):
   return render(request, 'about.html', {})

def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("secion iniciada"))
            return redirect('home')
        else:
            messages.success(request, ("Error! por favor intente otra vez"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    messages.success(request, ("cerraste secion"))
    return redirect('home')

