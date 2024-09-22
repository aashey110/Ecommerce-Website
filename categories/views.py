from django.shortcuts import render

# Create your views here.
def categories(request):
    data = {
        "title" : 'Categories'
    }
    return render(request, "categories.html", data)