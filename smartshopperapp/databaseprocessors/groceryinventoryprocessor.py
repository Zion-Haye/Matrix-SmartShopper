import csv
from smartshopperapp.models import GroceryInventory , GroceryDetails

def populate_grocery_inventory_database():
    grocery_inventory =GroceryInventory.objects.all()
    #print(products)

    if not grocery_inventory.exists():
        #print("None None None")

        with open('\grocery_inventory.csv') as csv_file:
            csv_reader = csv.reader(csv_file)

            #next(csv_reader)

            for row in csv_reader:
                grocery_name = row[0]
                branch_location = row[1]
                product_category = row[2]
                sub_category = row[3]
                brand_name = row[4]
                item_name = row[5]
                size = row[6]
                cost = row[7]
                image_url = row[8]

                grocery = GroceryDetails.objects.all().filter(grocery_name = grocery_name , branch_location = branch_location) 

                if grocery.exists():

                    grocery =  GroceryDetails.objects.get(grocery_name = grocery_name , branch_location = branch_location) 

                    groceryinventory = GroceryInventory(category=product_category , sub_category=sub_category,
                    brand_name = brand_name , item_name=item_name, size=size , cost=cost ,image=image_url , grocery = grocery)


                    try:
                        groceryinventory.save()
                        #product.commit()
                    except:
                        print("Error - Grocery Inventory")

                else:
                    print("Grocery: " , grocery_name , "does not exist")