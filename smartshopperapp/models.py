from operator import itemgetter
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

#notes
#null = true



# Create your models here.
class Product (models.Model):
    category = models.CharField(max_length=100 , null=True)
    sub_category = models.CharField(max_length=100, null=True)
    brand_name = models.CharField(max_length=100, null=True)
    full_item_name = models.CharField(max_length=100, null=True)
    item_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100 , null=True)
    quantity = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=200, null=True)
    

class Configuration (models.Model):
    priority = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)

class List (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True , default="Undefined")
    is_Active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE, null=True)

class ListItem (models.Model):
    list = models.ForeignKey(List,on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
    item_quantity = models.IntegerField(null=True)

#Add To Tests
class GroceryDetails(models.Model):
    grocery_name =  models.CharField(max_length=100 , null=False)
    branch_location =models.CharField(max_length=100 , null=True)

class GroceryInventory(models.Model):
    category = models.CharField(max_length=100 , null=True)
    sub_category = models.CharField(max_length=100, null=True)
    brand_name = models.CharField(max_length=100, null=True)
    item_name = models.CharField(max_length=100, null=True)
    size = models.CharField(max_length=100, null=True)
    cost = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=200, null=True)
    grocery = models.ForeignKey(GroceryDetails,on_delete=models.CASCADE, null=True)

class CityDetails(models.Model):
    city_name = models.CharField(max_length=100 , null=True)
    city_address = models.CharField(max_length=100 , null=True)
    



#Chnage product quantity to size?
