import csv
from smartshopperapp.models import GroceryDetails

def populate_grocery_detail_database():
    groceries = GroceryDetails.objects.all()
    #print(products)

    if not groceries.exists():
        #print("None None None")

        with open('smartshopperapp\datasheets\grocery_detail.csv') as csv_file:
            csv_reader = csv.reader(csv_file)

            #next(csv_reader)

            for row in csv_reader:
                grocery_name = row[0]
                branch_location = row[1]
             
                grocery_detail = GroceryDetails(grocery_name = grocery_name , branch_location= branch_location)

                try:
                    grocery_detail.save()
                    #product.commit()
                except:
                    print("Error -  Grocery Details")