from django.urls import path
from . import views

urlpatterns = [
    path('' , views.display_home_page , name="home" ),
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
    path('AddProductToList/',views.add_product_to_list , name="addproducttolist"),
    path('MyLists/',views.display_my_lists, name="display_my_last"),
    path('DeleteList/<list_id>/', views.delete_list , name="deletelist"),
    path('DeleteProductFromList/<product_id>/', views.delete_product_from_list , name="deleteproduct"),
    path('EditList/<list_id>/', views.edit_list_details , name="editdetailslist"),
    path('ViewListItems/<list_id>/', views.display_list_items , name="display_list_items")
    
]