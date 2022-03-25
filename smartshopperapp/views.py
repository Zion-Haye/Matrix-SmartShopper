import email
from itertools import product
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .databaseprocessors.productlistprocessor import *
from .databaseprocessors.listprocessor import *
from .databaseprocessors.listitemprocessor import *

# Create your views here.

def display_home_page(request):
    isauthenticated = request.user.is_authenticated
    print("In Home:")
    print("Is Authenticated: ", isauthenticated)


    populate_product_pool_database()

    return render (request, 'home.html')

def display_create_list_page(request):

    if request.method=="POST":
        listname = request.POST.get('listname')
        listdescription = request.POST.get('description')
       

        print("In Create List Post Request")
        print("listname: ",listname)
        print("description: ",listdescription)

        if request.user.is_authenticated:
            user = request.user
            create_list_registered_user(listname , listdescription , user)

        return  redirect ('/SelectCategory/')
    
    else:

        return render  (request , 'createlist.html')

def display_category_page(request):
    #Show all by default
    return render (request , 'selectcategory.html' )

def display_catalogue_page(request):
    products_by_category = get_products_by_category("Bread & Bakery")

    if request.user.is_authenticated:
        user = request.user
        activelist = get_registered_user_active_list(user)
        listitems = get_registered_user_list_items(activelist)
        print(listitems)
        #,{'listitems':listitems}

        return render (request , 'catalogue.html' , {'listitems':listitems} )


    return render (request , 'catalogue.html' , {'products':products_by_category})

def display_catalogue_page_with_category(request , category):
    print("Choosen Category: " , category)

    products_by_category = get_products_by_category(category)

    return render (request , 'catalogue.html', {'products':products_by_category})

def display_catalogue_page_with_subcategory(request , subcategory):

    print("In SubCategory")
    print(subcategory)
    products_by_sub_category = get_products_by_subcategory(subcategory)
    return render(request, 'catalogue.html', {'products':products_by_sub_category})

def display_search_results_page(request):
    return render (request, 'searchresult.html')

def display_account_page(request):

    if request.user.is_authenticated:
        user = request.user

        print('In Accounts')
        firstname = user.first_name
        lastname = user.last_name

    return render (request, 'accounts.html')

def display_configure_results_page(request):

    if request.method=="POST":
        priority = request.POST.get('priority')
        location= None

        if ((priority == "Closest") or (priority== "Cheapest and Closest")):
            location = request.POST.get('location')
        
        print("In Configure results POST")
        print(priority)
        print(location)

    return render (request, 'configureresults.html')

def add_product_to_list(request):

    if request.method=="POST":
        quantity = request.POST.get('product_quantity')
        product_id = request.POST.get('product_id')

        print("In Add Product To List")
        print(quantity)
        print(product_id)

        product = get_product_by_id(product_id)

        if request.user.is_authenticated:
            user = request.user
            activelist = get_registered_user_active_list(user)
            add_item_to_list_items(activelist , product ,quantity)

    return redirect('/Catalogue/')

def display_my_lists(request):
    
    if request.user.is_authenticated:
        user = request.user
        current_user_lists = get_registered_user_lists(user)

        return render(request ,  'displaylists.html' , {'lists':current_user_lists})



#Authentications views

def display_signup_page(request):

    if request.method=="POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password =  request.POST.get('password')

        print("In SignUp Post Request")
        print("Username: ",username)
        print("First Name: ",firstname)
        print("Last Name: ",lastname)
        print("Email: ",email)

        try:
            thisuser = User.objects.create_user(username, email , password)
            thisuser.first_name = firstname
            thisuser.last_name = lastname 

            thisuser.save()

            messages.success(request, "Account Succesfully Created")

            return redirect('/Login/')
        except:
            print("In SignuUp exception")
            return redirect('/SignUp/')
    
    else:
        print("Out Signup- Post request")

        return render(request,'signup.html')

def display_login_page(request):

    if request.method=="POST":
        username = request.POST.get('username')
        password =  request.POST.get('password')

        print("In Login Post Request")
        print("Username: ",username)

        try:
            user = authenticate(username=username , password=password)

            if user is not None:
                login(request, user)
                firstname = user.first_name
                lastname = user.last_name

            
                return render(request, "createlist.html" , {"firstname":firstname})
            
            else:
                messages.error(request,"Incorrect Credentials")
                return redirect ('/Login/')

        except:
                print("In Login Exception")

    return render (request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect("/")
    