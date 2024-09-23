from django.shortcuts import render
from product.models import Banners

def index(request):
    all_banners = Banners.objects.all()
    data = {
        "title" : 'Home',
        "banner": all_banners,
    }
    return render(request, 'index.html', data)

def about(request):
    data = {
        "title" : 'About'
    }
    return render(request, 'about.html', data)

def contact(request):
    data = {
        "title" : 'Contact Us'
    }
    return render(request, 'contact.html', data)


