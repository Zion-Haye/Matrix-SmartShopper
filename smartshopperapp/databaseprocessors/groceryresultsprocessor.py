import csv
from smartshopperapp.models import GroceryDetails , GroceryInventory , ListItem
from smartshopperapp.distancecalculator.distancecalculator import *



def get_grocery_results(activelist,listitems):
    all_grocery_results_list = []

    #grocery = GroceryDetails.objects.get(grocery_name="Tru Valu",branch_location="Trincity Mall, Piarco")
    #print('Grocery')
    #print(grocery.grocery_name , grocery.branch_location)

    all_groceries = GroceryDetails.objects.all()

    if all_groceries.exists():
        for grocery in all_groceries:
            grocery_inventory = get_grocery_inventory(grocery)
            grocery_result = get_individual_grocery_result(grocery_inventory , grocery , listitems , activelist)
            all_grocery_results_list.append(grocery_result)

    #print("All results")
    #print (all_grocery_results_list)

    return all_grocery_results_list

    




def get_individual_grocery_result(grocery_inventory , grocery , listitems , activelist):
    grocery_result ={}
    grocery_result["grocery_name"] = grocery.grocery_name
    grocery_result["branch_location"] = grocery.branch_location

    num_found = 0
    num_not_found = 0
    total_cost = 0

    grocery_items = []

    for listitem in listitems:
        #print("Listitem : Brand name")
        #print(listitem.product.brand_name)

        grocery_inventory_by_brand_name = GroceryInventory.objects.all().filter(brand_name  = listitem.product.brand_name , grocery = grocery)
        #print("Inventory By brandName")
        #print(grocery_inventory_by_brand_name)

        isFound = False
    
        if grocery_inventory_by_brand_name.exists():

            for inventory_item in grocery_inventory_by_brand_name:

                #print("Inventory Item")
                #print(inventory_item.brand_name , inventory_item.item_name)

                does_contain_item = contains_item(inventory_item.item_name , listitem.product.item_name)

                if does_contain_item == True:

                    does_contain_description = contains_description(inventory_item.item_name  , listitem.product.description)

                    if does_contain_description == True:

                        total_item_cost = int(listitem.item_quantity) * float(inventory_item.cost)

                        grocery_item = {
                            'item_name' : inventory_item.item_name,
                            'quantity' :listitem.item_quantity,
                            'unit_price': inventory_item.cost,
                            'total_cost' : total_item_cost
                        }

                        grocery_items.append(grocery_item)

                        num_found = num_found + 1
                        total_cost = total_cost + total_item_cost

                        isFound = True
                
            if not isFound:
                grocery_item = {
                    'item_name' : listitem.product.full_item_name,
                    'quantity' :listitem.item_quantity,
                    'unit_price': "-",
                    'total_cost' :"-"
                }

                grocery_items.append(grocery_item)

                num_not_found = num_not_found + 1



        else:
            grocery_item = {
                'item_name' : listitem.product.full_item_name,
                'quantity' :listitem.item_quantity,
                'unit_price': "-",
                'total_cost' :"-"
            }

            grocery_items.append(grocery_item)

            num_not_found = num_not_found + 1

    grocery_result["grocery_items"] = grocery_items
    grocery_result["num_found"] = num_found
    grocery_result["num_not_found"] = num_not_found
    grocery_result["total_cost"] = total_cost

    #googleAPIresponse = get_google_response(grocery.branch_location , activelist.configuration.location)

    #grocery_result["distance"] = googleAPIresponse["distance"]
    #grocery_result["duration"] = googleAPIresponse["duration"]

    grocery_result["distance"] = "Disconnected"
    grocery_result["duration"] = "Disconnected"

    #print(grocery_result)

    return grocery_result


def contains_item(inventory_full_item_name , list_item_name):

    inventory_full_item_name = inventory_full_item_name.lower()
    list_item_name = list_item_name.lower()
    
    if list_item_name in inventory_full_item_name:
        return True

    list_item_name_split  = list_item_name.split()
    
    if list_item_name_split:

        for word in list_item_name_split:
            if word in inventory_full_item_name:
                return True
    
    
    return False

def contains_size(inventory_full_item_name , list_item_description):

   return False

def contains_description(inventory_full_item_name , list_item_description):
    inventory_full_item_name = inventory_full_item_name.lower()
    list_item_description = list_item_description.lower()

    if list_item_description in inventory_full_item_name:
        return True
    
    list_item_description_split = list_item_description.split()

    if list_item_description_split:
        for word in list_item_description_split:
            if word in inventory_full_item_name:
                return True

    return False


def get_grocery_inventory(grocery):
    grocery_inventory = GroceryInventory.objects.all().filter(grocery = grocery)

    if grocery_inventory.exists():
        return grocery_inventory
    else:
        return None

