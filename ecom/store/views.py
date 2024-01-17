from django.shortcuts import render, redirect
from .models import Product, Category, Face
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
    products = Product.objects.all()[:4]
    return render(request, 'home.html', {'products':products})


def about(request):
   return render(request, 'about.html', {})


def planos(request):
    categoria_filtro = request.GET.get('categoria', '')
    ancho_terreno_filtro = request.GET.get('ancho_terreno', '')
    metros_cuadrados_filtro = request.GET.get('metros_cuadrados', '')
    dormitorios_filtro = request.GET.get('dormitorios', '')
    pisos_filtro = request.GET.get('pisos', '')

    products = Product.objects.all()

    if categoria_filtro:
        products = products.filter(category=categoria_filtro)
    
    if ancho_terreno_filtro:
        products = products.filter(width=int(ancho_terreno_filtro))

    if metros_cuadrados_filtro:
        products = products.filter(dimension=int(metros_cuadrados_filtro))

    if dormitorios_filtro:
        products = products.filter(cantRoom=int(dormitorios_filtro))

    if pisos_filtro:
        products = products.filter(cantFloor=int(pisos_filtro))

    categories = Category.objects.all()
    return render(request, 'planos.html', {'products': products, 'categories': categories})


def fachadas(request):
    categoria_filtro = request.GET.get('categoria', '')
    faces = Face.objects.all()
    if categoria_filtro:
        faces = faces.filter(category=categoria_filtro)
    categories = Category.objects.all()
    return render(request, 'fachadas.html', {'faces':faces, 'categories': categories})