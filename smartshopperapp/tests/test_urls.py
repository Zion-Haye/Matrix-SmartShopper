
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from smartshopperapp.views import *

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url =  reverse('home')
        self.assertEquals(resolve(url).func , display_home_page)

    def test_create_list_url_resolves(self):
        url =  reverse('create_list')
        self.assertEquals(resolve(url).func , display_create_list_page)
    
    def test_home_select_category_resolves(self):
        url =  reverse('select_category')
        self.assertEquals(resolve(url).func , display_category_page)

    def test_display_catalogue_url_resolves(self):
        url =  reverse('display_catalogue')
        self.assertEquals(resolve(url).func , display_catalogue_page)

    def test_display_catalogue_with_category_url_resolves(self):
        url =  reverse('display_catalogue_category' , args=['Bakery'])
        self.assertEquals(resolve(url).func , display_catalogue_page_with_category)

    def test_login_url_resolves(self):
        url =  reverse('login')
        self.assertEquals(resolve(url).func , display_login_page)

    def test_signup_url_resolves(self):
        url =  reverse('signup')
        self.assertEquals(resolve(url).func , display_signup_page)

    def test_logout_url_resolves(self):
        url =  reverse('logout')
        self.assertEquals(resolve(url).func , logout_user)

    def test_accounts_url_resolves(self):
        url =  reverse('accounts')
        self.assertEquals(resolve(url).func , display_account_page)

    def test_search_results_url_resolves(self):
        url =  reverse('search_results')
        self.assertEquals(resolve(url).func , display_search_results_page)

    def test_configure_results_url_resolves(self):
        url =  reverse('configure_results')
        self.assertEquals(resolve(url).func , display_configure_results_page)

    def test_display_catalogue_subcategory_url_resolves(self):
        url =  reverse('display_catalogue_subcategory', args=['Fruits'])
        self.assertEquals(resolve(url).func , display_catalogue_page_with_subcategory)

    def test_add_product_to_list_url_resolves(self):
        url =  reverse('add_product_to_list')
        self.assertEquals(resolve(url).func , add_product_to_list)

    def test_display_my_lists_url_resolves(self):
        url =  reverse('display_my_lists')
        self.assertEquals(resolve(url).func , display_my_lists)

    def test_delete_list_url_resolves(self):
        url =  reverse('delete_list', args=['1'])
        self.assertEquals(resolve(url).func , delete_list)

    def test_delete_product_from_list_url_resolves(self):
        url =  reverse('delete_product', args=['1'])
        self.assertEquals(resolve(url).func , delete_product_from_list)

    def test_edit_list_details_url_resolves(self):
        url =  reverse('edit_list_details', args=['1'])
        self.assertEquals(resolve(url).func , edit_list_details)

    def test_display_list_items_url_resolves(self):
        url =  reverse('display_list_items', args=['1'])
        self.assertEquals(resolve(url).func , display_list_items)

    def test_edit_user_details_url_resolves(self):
        url =  reverse('edit_user_details')
        self.assertEquals(resolve(url).func , edit_user_details)

    def test_change_user_password_url_resolves(self):
        url =  reverse('change_user_password')
        self.assertEquals(resolve(url).func , change_user_password )

    def test_make_list_active_url_resolves(self):
        url =  reverse('make_list_active', args=['1'])
        self.assertEquals(resolve(url).func , make_list_active)

    def test_display_grocery_resultse_url_resolves(self):
        url =  reverse('display_grocery_results')
        self.assertEquals(resolve(url).func , display_grocery_results)

    def test_delete_account_url_resolves(self):
        url =  reverse('delete_account')
        self.assertEquals(resolve(url).func ,delete_account )

    def test_update_product_quantity_from_catalogue_url_resolves(self):
        url =  reverse('update_product_quantity_from_catalogue')
        self.assertEquals(resolve(url).func , update_product_quantity_from_catalogue)

    def test_select_list_url_resolves(self):
        url =  reverse('select_list',args=['1'])
        self.assertEquals(resolve(url).func , select_list )

    def test_remove_item_from_mylis_url_resolves(self):
        url =  reverse('remove_item_from_mylist',args=['1','1'])
        self.assertEquals(resolve(url).func , remove_item_from_mylist)

    def test_update_item_from_mylist_url_resolves(self):
        url =  reverse('update_item_from_mylist')
        self.assertEquals(resolve(url).func ,update_item_from_mylist )

    