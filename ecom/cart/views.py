from django.shortcuts import render

def cartSumary(request):
    return render(request, 'cartSumary.html', {})


def cartAdd(request):
    pass

def cartDelete(request):
    pass

def cartUpdate(request):
    pass