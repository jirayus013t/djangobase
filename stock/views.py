from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render (request, 'frontend/index.html', {'products': products})

def about(request):
    return render(request, 'frontend/about.html')

def contact(request):
    products = Product.objects.all()
    return render(request, 'frontend/contact.html',{'products': products} )

def mplaces(request):
    return render(request, 'frontend/mplaces.html')

def mcreatures(request):
    return render(request, 'frontend/mcreatures.html')

def maliens(request):
    return render(request, 'frontend/maliens.html')

def time(request):
    return render(request, 'frontend/time.html')
