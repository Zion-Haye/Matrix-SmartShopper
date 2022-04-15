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

def get_product_by_id(product_id):
     
    product = Product.objects.all().filter(id=product_id)
    

    if product.exists():
        product = Product.objects.get(id=product_id)
        return product
    else:
        return None

def get_products_by_search(search_text):

    search_results = Product.objects.all().filter(full_item_name__icontains=search_text)

    if search_results.exists():
        return search_results
    else:
        return None

def populate_product_pool_database():
    products = Product.objects.all()
    #print(products)

    if not products.exists():
        #print("None None None")

        with open('smartshopperapp\datasheets\display_sample.csv') as csv_file:
            csv_reader = csv.reader(csv_file)

            #next(csv_reader)

            for row in csv_reader:
                product_category = row[2]
                sub_category = row[3]
                brand_name = row[4]
                full_item_name = row[0]
                item_name = row[5]
                quantity = row[1]
                image_url = row[7]
                description = row[6]

                product = Product(category=product_category , sub_category=sub_category,
                brand_name = brand_name , full_item_name=full_item_name,
                item_name=item_name, description=description , quantity=quantity,image=image_url)

                try:
                    product.save()
                    #product.commit()
                except:
                    print("Error")


""" product_category = row[0]
                sub_category = row[1]
                brand_name = row[2]
                full_item_name = row[3]
                item_name = row[4]
                quantity = row[5]
                image_url = row[6] """