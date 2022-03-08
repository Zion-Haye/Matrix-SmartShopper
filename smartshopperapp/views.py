import email
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def display_home_page(request):
    isauthenticated = request.user.is_authenticated
    print("In Home:")
    print("Is Authenticated: ", isauthenticated)
    return render (request, 'home.html')

def display_create_list_page(request):

    if request.method=="POST":
        listname = request.POST.get('listname')
        description = request.POST.get('description')
       

        print("In Create List Post Request")
        print("listname: ",listname)
        print("description: ",description)

        return  redirect ('/SelectCategory/')
    
    else:

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

def display_search_results_page(request):
    return render (request, 'searchresult.html')

def display_account_page(request):
    return render (request, 'accounts.html')


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
    