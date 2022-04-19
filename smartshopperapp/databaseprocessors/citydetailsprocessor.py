import csv
from smartshopperapp.models import CityDetails

def populate_city_detail_database():


    cities = CityDetails.objects.all()

    #print(products)

    if not cities.exists():
        #print("None None None")

        with open('city_address.csv') as csv_file:
            csv_reader = csv.reader(csv_file)

            #next(csv_reader)

            for row in csv_reader:
                city_name = row[0]
                city_address = row[3]
             
                city_detail = CityDetails(city_name=city_name , city_address=city_address)

                try:
                    city_detail.save()
                    #product.commit()
                except:
                    print("Error - City Details")