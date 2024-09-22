from django.shortcuts import render

def index(request):
    data = {
        "title" : 'Home'
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


