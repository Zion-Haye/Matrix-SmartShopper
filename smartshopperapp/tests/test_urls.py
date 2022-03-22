
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


    

