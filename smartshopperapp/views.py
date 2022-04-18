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
from .databaseprocessors.grocerydetailprocessor import *
from .databaseprocessors.groceryinventoryprocessor import *
from .databaseprocessors.groceryresultsprocessor import *
from .databaseprocessors.citydetailsprocessor import *
from .distancecalculator.distancecalculator import *

# Create your views here.

#Pages
def display_home_page(request):
    isauthenticated = request.user.is_authenticated
    print("In Home:")
    print("Is Authenticated: ", isauthenticated)

    #product = Product.objects.all()
    #product.delete()
    
    #populate_grocery_detail_database()
    #populate_grocery_inventory_database()

    #user = User.objects.get(username="johndoe")
    #user.set_password("password")
    #user.save()

    print("before populate city")
    populate_city_detail_database()
    print("after populate city")

    #cities = CityDetails.objects.all()
    #ities.delete()

    #test_dc()

    print("before populate product pool")
    populate_product_pool_database()
    print("after populat product pool")

    print("Right before return render")
    return render (request, 'templates/home.html')

def display_category_page(request):
    return render (request , 'selectcategory.html' )

def display_catalogue_page(request):
    products_by_category = get_products_by_category("Bread & Bakery")

    if request.user.is_authenticated:
        user = request.user
        activelist = get_registered_user_active_list(user)
        listitems = get_list_items(activelist)
        activelistcount =get_num_items_in_list_item(activelist)

        context={
            'products':products_by_category, 
            'listitems':listitems, 
            'confirmlistitems':listitems,
            'activelist':activelist,
            'activelistcount': activelistcount
        }

        return render (request , 'catalogue.html' , context )


    return render (request , 'catalogue.html' , {'products':products_by_category})

def display_catalogue_page_with_category(request , category):
    print("Choosen Category: " , category)

    products_by_category = get_products_by_category(category)

    if request.user.is_authenticated:
        user = request.user
        activelist = get_registered_user_active_list(user)
        listitems = get_list_items(activelist)
        activelistcount =get_num_items_in_list_item(activelist)

        context={
            'products':products_by_category, 
            'listitems':listitems, 
            'confirmlistitems':listitems,
            'activelist':activelist,
            'activelistcount': activelistcount,
            'category':category
        }

        return render (request , 'catalogue.html', context)

    else:
        context={
            'products':products_by_category 
        }

        return render (request , 'catalogue.html', context)


def display_catalogue_page_with_subcategory(request , subcategory):

    print("In SubCategory")
    print(subcategory)
    products_by_sub_category = get_products_by_subcategory(subcategory)

    if request.user.is_authenticated:
        user = request.user
        activelist = get_registered_user_active_list(user)
        listitems = get_list_items(activelist)
        activelistcount =get_num_items_in_list_item(activelist)

        context={
            'products':products_by_sub_category, 
            'listitems':listitems, 
            'confirmlistitems':listitems,
            'activelist':activelist,
            'activelistcount': activelistcount,
            'category': subcategory

        }
    
        return render(request, 'catalogue.html', context)

    else:
        context={
            'products':products_by_sub_category
        }
    
        return render(request, 'catalogue.html', context)


def display_search_results_page(request):
    print("In Search Results")
    if request.method=="POST":
        search_text = request.POST.get('search')
        search_results = get_products_by_search(search_text)
        print(search_text)

        if request.user.is_authenticated:
            user = request.user
            activelist = get_registered_user_active_list(user)
            listitems = get_list_items(activelist)

            context={
                'products':search_results, 
                'listitems':listitems, 
                'confirmlistitems':listitems,
                'activelist':activelist
            }
    
        else:

            context={
                'products':search_results
            }


    return render (request, 'catalogue.html', context)

def display_configure_results_page(request):

    if request.method=="POST":
        priority = request.POST.get('priority')
        location = request.POST.get('location')

        if request.user.is_authenticated:
            user = request.user
            activelist = get_registered_user_active_list(user)

            configuration = Configuration(priority=priority , location =location)
            configuration.save()

            activelist.configuration = configuration
            activelist.save()
        
        print("In Configure results POST")
        print(priority)
        print(location)





        return redirect ('/GroceryResults/')
    
    cities = CityDetails.objects.all()

    context = {
        'cities': cities
    }

    return render (request, 'configureresults.html' , context)


def display_grocery_results(request):
    if request.user.is_authenticated:
        user = request.user
        activelist = get_registered_user_active_list(user)
        listitems = get_list_items(activelist)

        groceryresults = get_grocery_results(activelist ,listitems)

        context={
                'groceryresults':groceryresults
            }

        return render (request, 'groceryresults.html' , context)




# Product and List
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

        if request.user.is_authenticated:
            user = request.user
            current_user_lists = get_registered_user_lists(user)

            return render  (request , 'createlist.html', {'lists':current_user_lists})


        return render  (request , 'createlist.html')

def add_product_to_list(request):

    #where to redirect when theres no active list to add to

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

def update_product_quantity_from_catalogue(request):
    if request.user.is_authenticated:
        user = request.user
        activelist = get_registered_user_active_list(user)

        if request.method=="POST":
            quantity = request.POST.get('product_quantity')
            product_id = request.POST.get('product_id')

            product = get_product_by_id(product_id)

            update_list_item_quantity(activelist , product, quantity)

            return redirect('/Catalogue/')


def display_my_lists(request):
    
    if request.user.is_authenticated:
        user = request.user
        current_user_lists = get_registered_user_lists(user)

        return render(request ,  'displaylists.html' , {'lists':current_user_lists})

def delete_list(request , list_id):

    if request.user.is_authenticated:
        user = request.user
        delete_list_by_id(list_id,user)

        return redirect('/MyLists/')

def delete_product_from_list(request, product_id):

    print("In Delete product from list")

    if request.user.is_authenticated:
        user = request.user
        activelist = get_registered_user_active_list(user)
        product = get_product_by_id(product_id)
        delete_item_from_list_item(activelist , product)

        return redirect ('/Catalogue/')

def edit_list_details(request, list_id):
    if request.user.is_authenticated:
        user = request.user
        current_user_lists = get_registered_user_lists(user)

        if request.method=="POST":

            list_name = request.POST.get('listname')
            list_description = request.POST.get('description')

            edit_list_object_details(list_id, list_name, list_description)

            current_user_lists = get_registered_user_lists(user)
            context={
                'lists':current_user_lists
            }

        else:

            list_to_edit = find_list_by_id(list_id)
            context={
                'lists':current_user_lists,
                'listtoedit': list_to_edit
            }

        return render(request ,  'displaylists.html' , context)

def display_list_items(request , list_id):
    if request.user.is_authenticated:
        user = request.user
        current_user_lists = get_registered_user_lists(user)
        list = find_list_by_id(list_id)
        list_items = get_list_items(list)

        context={
            'lists':current_user_lists,
            'listitems':list_items
        }

        return render(request ,  'displaylists.html' , context)

def make_list_active(request , list_id):

    if request.user.is_authenticated:
        user = request.user

        set_list_to_active(list_id , user)

        return redirect ('/MyLists/')

def select_list(request , list_id):

    if request.user.is_authenticated:
        user = request.user

        set_list_to_active(list_id , user)

        return redirect ('/SelectCategory/')


def remove_item_from_mylist(request , list_id , product_id):

    if request.user.is_authenticated:
        #user = request.user

        print("Remove item from mylist")
        print(list_id)
        print(product_id)

        list = find_list_by_id(list_id)
        product = get_product_by_id(product_id)

        delete_item_from_list_item(list , product)

        return redirect ('/ViewListItems/' + list_id + '/')


def update_item_from_mylist (request):
    if request.user.is_authenticated:
        #user = request.user
        if request.method=="POST":

            list_id = request.POST.get('list_id')
            product_id = request.POST.get('product_id')
            quantity = request.POST.get('product_quantity')

            print("Update item from mylist")
            print(list_id)
            print(product_id)
            print(quantity)

            list = find_list_by_id(list_id)
            product = get_product_by_id(product_id)

            update_list_item_quantity(list , product, quantity)

            return redirect ('/ViewListItems/' + list_id + '/')
   

#User Account
def display_account_page(request):

    if request.user.is_authenticated:
        user = request.user

    return render (request, 'accounts.html')

def edit_user_details(request):
    if request.user.is_authenticated:
        user = request.user

        if request.method=="POST":
            username = request.POST.get('username')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')

            #Move To Seperate File?
            user.username = username
            user.first_name = firstname
            user.last_name = lastname
            user.email = email

            user.save()


            return redirect ('/Accounts/')

def change_user_password(request):
    if request.user.is_authenticated:
        user = request.user

        if request.method=="POST":
            password =  request.POST.get('password')
            user.set_password(password)
            user.save()
            messages.success(request,"Password Changed Successfully!")
            return redirect ('/Login/')




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

            
                return redirect ('/CreateList/')
            
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
    

def delete_account(request):

    if request.user.is_authenticated:
        user = request.user
        user.delete()
        messages.success(request,"Account Deleted Successfully!")
        return redirect("/")
