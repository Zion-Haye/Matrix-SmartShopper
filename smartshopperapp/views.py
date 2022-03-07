from django.shortcuts import render

# Create your views here.

def display_home_page(request):
    return render (request, 'home.html')

def display_create_list_page(request):
    return render  (request , 'createlist.html')

def display_category_page(request):
    return render (request , 'selectcategory.html' )

def display_catalogue_page(request , category):
    print("Choosen Category: " , category)

    #category = {}
    #category['category']=category

    #return render (request , 'catalogue.html' , {'title': 'Portfolio'})
    #return render (request , 'catalogue.html' , category)

    #Look into emplate respone
    return render (request , 'catalogue.html')