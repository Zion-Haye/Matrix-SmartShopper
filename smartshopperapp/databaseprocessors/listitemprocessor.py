from smartshopperapp.models import *


def add_item_to_list_items(list , product, quantity):

    listitem = ListItem.objects.all().filter(list=list , product=product)
    

    if listitem.exists():
        listitem= ListItem.objects.get(list=list , product=product)
        listitem.item_quantity = listitem.item_quantity + 1
        listitem.save()

    else:
        if (list!=None) and (product!=None):
            listitem = ListItem(list=list , product=product , item_quantity=quantity)
            listitem.save()

def update_list_item_quantity(list , product, quantity):
    listitem = ListItem.objects.all().filter(list=list , product=product)
    

    if listitem.exists():
        listitem= ListItem.objects.get(list=list , product=product)

        if quantity!= 0:
            listitem.item_quantity = quantity
            listitem.save()

        else:
            delete_item_from_list_item(list , product)



def get_list_items(list):
    active_list_items = ListItem.objects.all().filter(list=list)

    if active_list_items.exists():
        return active_list_items
    else:
        return None

def delete_item_from_list_item(list , product):

    if (list!=None) and (product!=None):
        listitem = ListItem.objects.all().filter(list=list , product=product)
    
        if listitem.exists():
            listitem = ListItem.objects.get(list=list , product=product)
            listitem.delete()

        #look into delete , do i need to save?

def get_num_items_in_list_item(list):

    if list == None:
        return 0
    
    else:
        listitemcount = ListItem.objects.all().filter(list=list).count()
        return listitemcount

