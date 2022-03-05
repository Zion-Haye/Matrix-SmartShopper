from django.shortcuts import render

# Create your views here.

def display_home_page(request):
    return render (request, 'home.html')

def display_create_list_page(request):
    return render  (request , 'createlist.html')

def display_category_page(request):
    return render (request , 'selectcategory.html' )
