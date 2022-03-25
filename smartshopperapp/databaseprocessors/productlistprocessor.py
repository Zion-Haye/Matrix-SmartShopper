import csv
from smartshopperapp.models import Product

def get_products_by_category(category):

    if category != "All":
        products_by_category = Product.objects.all().filter(category=category)        
    else :
        products_by_category = Product.objects.all()
    
    if products_by_category.exists():
        return products_by_category
    else:
        return None


def get_products_by_subcategory(subcategory):
   
    products_by_sub_category = Product.objects.all().filter(sub_category=subcategory)        
 
    if products_by_sub_category.exists():
        return products_by_sub_category
    else:
        return None



def populate_product_pool_database():
    products = Product.objects.all()
    print(products)

    if not products.exists():
        print("None None None")

        with open('smartshopperapp\datasheets\productpoolv1.csv') as csv_file:
            csv_reader = csv.reader(csv_file)

            #next(csv_reader)

            for row in csv_reader:
                product_category = row[0]
                sub_category = row[1]
                brand_name = row[2]
                full_item_name = row[3]
                item_name = row[4]
                quantity = row[5]
                image_url = row[6]

                product = Product(category=product_category , sub_category=sub_category,
                brand_name = brand_name , full_item_name=full_item_name,
                item_name=item_name,quantity=quantity,image=image_url)

                try:
                    product.save()
                    #product.commit()
                except:
                    print("Error")