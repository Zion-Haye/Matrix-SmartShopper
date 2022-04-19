from django.urls import path
from . import views

urlpatterns = [
    path('' , views.display_home_page , name="home" ),
    path('About/', views.display_about_us , name="about_us" ),
    path('CreateList/' , views.display_create_list_page,name="create_list"),
    path('SelectCategory/', views.display_category_page, name="select_category"),
    path('Catalogue/' , views.display_catalogue_page, name="display_catalogue"),
    path('Catalogue/Category/<category>/' , views.display_catalogue_page_with_category, name="display_catalogue_category"),
    path('Login/', views.display_login_page, name="login"),
    path('SignUp/',views.display_signup_page, name="signup"),
    path('Logout/', views.logout_user , name="logout"),
    path('Accounts/',views.display_account_page, name="accounts"),
    path('SearchResults/',views.display_search_results_page, name="search_results"),
    path('ConfigureResults/',views.display_configure_results_page, name="configure_results"),

    path('Catalogue/SubCategory/<subcategory>/',views.display_catalogue_page_with_subcategory, name="display_catalogue_subcategory"),
    path('AddProductToList/',views.add_product_to_list , name="add_product_to_list"),
    path('MyLists/',views.display_my_lists, name="display_my_lists"),
    path('DeleteList/<list_id>/', views.delete_list , name="delete_list"),
    path('DeleteProductFromList/<product_id>/', views.delete_product_from_list , name="delete_product"),
    path('EditList/<list_id>/', views.edit_list_details , name="edit_list_details"),
    path('ViewListItems/<list_id>/', views.display_list_items , name="display_list_items"),
    path('EditUserDetails/', views.edit_user_details , name="edit_user_details"),
    path('ChangeUserPassword/', views.change_user_password, name="change_user_password"),
    path('MakeListActive/<list_id>/', views.make_list_active, name="make_list_active"),

    path('GroceryResults/',views.display_grocery_results, name="display_grocery_results"),
    path('DeleteAccount/', views.delete_account, name="delete_account"),
    path('Catalogue/UpdateItem/', views.update_product_quantity_from_catalogue , name="update_product_quantity_from_catalogue"),
    path('SelectList/<list_id>/', views.select_list , name="select_list"),


    path('MyLists/RemoveItem/<list_id>/<product_id>/',views.remove_item_from_mylist, name="remove_item_from_mylist"),
    path('MyLists/UpdateItem/',views.update_item_from_mylist, name="update_item_from_mylist"),

    path('AboutUs/', views.display_about_us , name="views.display_about_us" )
    
]