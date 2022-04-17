from django.test import TestCase
from smartshopperapp.models import Product, Configuration , List , ListItem
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            category = "Fresh Produce",
            sub_category = "Vegetables",
            brand_name = "Green Giant",
            full_item_name = "GREEN GIANT KLONDIKE  GOURMET POTATOES RED",
            item_name = "KLONDIKE  GOURMET POTATOES RED",
            description = "RED",
            quantity = "1 ea",
            image = "https://shop.doortodoortt.com/trincity/wp-content/uploads/2020/12/GREEN-GIANT-KLONDIKE-GOURMET-POTATOES-RED.jpg"
        )

        self.user = User.objects.create(
            first_name = "John",
            last_name = "Doe",
            username = "johndoe",
            email = "johndoe@gmail.com"
        )

        self.configuration = Configuration.objects.create(
            priority = "Cheapest",
            location = "Arima"
        )

 
        self.list = List.objects.create(
            name = "Birthday List",
            description = "Items for my 21st Birthday Party",
            user = self.user,
            configuration = self.configuration
        )

        self.listItem = ListItem.objects.create(
            list = self.list,
            product = self.product,
            item_quantity = 1
        )


    #User
    def test_user_first_name_is_assigned_on_creation(self):
        self.assertEquals(self.user.first_name, "John")

    def test_user_last_name_is_assigned_on_creation(self):
        self.assertEquals(self.user.last_name, "Doe")

    def test_user_username_is_assigned_on_creation(self):
        self.assertEquals(self.user.username, "johndoe")
    
    def test_user_email_is_assigned_on_creation(self):
        self.assertEquals(self.user.email, "johndoe@gmail.com")

    #Product Test
    def test_product_category_is_assigned_on_creation(self):
        self.assertEquals(self.product.category, "Fresh Produce")

    def test_product_sub_category_is_assigned_on_creation(self):
        self.assertEquals(self.product.sub_category, "Vegetables")

    def test_product_brand_name_is_assigned_on_creation(self):
        self.assertEquals(self.product.brand_name, "Green Giant")

    def test_product_full_item_name_is_assigned_on_creation(self):
        self.assertEquals(self.product.full_item_name, "GREEN GIANT KLONDIKE  GOURMET POTATOES RED")

    def test_product_item_name_is_assigned_on_creation(self):
        self.assertEquals(self.product.item_name, "KLONDIKE  GOURMET POTATOES RED")

    def test_quantity_is_assigned_on_creation(self):
        self.assertEquals(self.product.quantity, "1 ea")

    def test_product_image_is_assigned_on_creation(self):
        self.assertEquals(self.product.image, "https://shop.doortodoortt.com/trincity/wp-content/uploads/2020/12/GREEN-GIANT-KLONDIKE-GOURMET-POTATOES-RED.jpg")

    def test_description_is_assigned_on_creation(self):
        self.assertEquals(self.product.description, "RED")
    
    #Configuration
    def test_configuration_priority_is_assigned_on_creation(self):
        self.assertEquals(self.configuration.priority, "Cheapest")
                                   
    def test_configuration_location_is_assigned_on_creation(self):
        self.assertEquals(self.configuration.location, "Arima")


    #List    
    def test_list_name_is_assigned_on_creation(self):
        self.assertEquals(self.list.name, "Birthday List")

    def test_list_description_is_assigned_on_creation(self):
        self.assertEquals(self.list.description, "Items for my 21st Birthday Party")

    def test_list_is_active_is_assigned_on_creation(self):
        self.assertTrue(self.list.is_Active)

    def test_list_user_is_assigned_on_creation(self):
        self.assertEquals(self.list.user, self.user)

    def test_list_configuration_is_assigned_on_creation(self):
        self.assertEquals(self.list.configuration, self.configuration)

    #List Items
    def test_list_item_list_is_assigned_on_creation(self):
        self.assertEquals(self.listItem.list, self.list)

    def test_list_item_product_is_assigned_on_creation(self):
        self.assertEquals(self.listItem.product, self.product)

    def test_list_item_item_quantity_is_assigned_on_creation(self):
        self.assertEquals(self.listItem.item_quantity, 1)