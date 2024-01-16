from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages

def category(request, foo):
    # Replace Hyphens with spaces
    foo = foo.replace('-', ' ')
    # Grab the category from the url
    try:
        # Look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("Esa categoria no existe"))
        return redirect('home')


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})


def about(request):
   return render(request, 'about.html', {})
