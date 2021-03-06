from smartshopperapp.models import *
from django.contrib.auth.models import User

def create_list_registered_user(list_name , list_description , user):

    print("In Create List Registered User")
    print(list_name)
    print(list_description)

    previous_active_list = List.objects.all().filter(user=user , is_Active="True")

    if not previous_active_list.exists():
        new_active_list = List(name=list_name , description=list_description,
                            is_Active="True",user=user)
        new_active_list.save()
    
    else:
        previous_active_list = List.objects.get(user=user , is_Active="True")
        previous_active_list.is_Active = "False"
        previous_active_list.save()

        new_active_list = List(name=list_name , description=list_description,
                            is_Active="True",user=user)
        new_active_list.save()

def get_registered_user_lists(user):

    current_user_list = List.objects.all().filter(user=user)

    if current_user_list.exists():
        return current_user_list
    else:
        return None


def get_registered_user_active_list(user):
    current_user_active_list = List.objects.all().filter(user=user , is_Active="True")

    if current_user_active_list.exists():
        current_user_active_list = List.objects.get(user=user , is_Active="True")
        return current_user_active_list

    else:
        return None

def find_list_by_id(list_id):
    list = List.objects.all().filter(id=list_id)

    if list.exists():
        list = List.objects.get(id=list_id)
        return list
    
    else:
        return None

def delete_list_by_id(list_id,user):
    list = List.objects.all().filter(id=list_id)
  
    if list.exists():
        list = List.objects.get(id=list_id)
        list.delete()
 
        if list.is_Active==True:
            current_user_lists = get_registered_user_lists(user)

            if current_user_lists != None:
                last_created_list = List.objects.filter(user=user).last()
                last_created_list.is_Active = "True"
                last_created_list.save()
        
            
def edit_list_object_details(list_id, list_name, list_description):
    list = find_list_by_id(list_id)

    if list!=None:
        list.name = list_name
        list.description = list_description
        list.save()


def get_registered_user_active_list_count(user):
    num_items 
    pass
    
    

def set_list_to_active(list_id , user):

    list = find_list_by_id(list_id)

    if list != None:

        previous_active_list = get_registered_user_active_list(user)
        previous_active_list.is_Active = "False"
        previous_active_list.save()

        new_active_list = list
        new_active_list.is_Active = "True"
        new_active_list.save()




#what if i delete the active list