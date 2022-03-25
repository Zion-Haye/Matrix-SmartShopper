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

    
    