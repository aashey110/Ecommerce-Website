from django.shortcuts import render
from product.models import Product, Categories
# Create your views here.

def products(request):
    all_products = Product.objects.all()
    data = {
        "title" : 'Products',
        "products" : all_products,
    }
    
    return render(request, "product.html", data)

def categories(request):
    all_categories = Categories.objects.all()
    data = {
        "title" : 'Categories',
        "categories": all_categories,
    }
    return render(request, "categories.html", data)


def productDetail(request, id):
    single_product = Product.objects.filter(id = id)
    all_products = Product.objects.all()

    data = {
        "product" : single_product,
        "products" : all_products,
    }
    return render(request, "single_product.html", data)
















