from django.urls import path
from . import views

urlpatterns = [
    path('' , views.display_home_page , name="home" ),
    path('CreateList/' , views.display_create_list_page,name="createlist"),
    path('SelectCategory/', views.display_category_page, name="selectcategory"),
    path('Catalogue/' , views.display_catalogue_page),
    path('Catalogue/<category>/' , views.display_catalogue_page_with_category),
    path('Login/', views.display_login_page, name="login"),
    path('SignUp/',views.display_signup_page, name="signup"),
    path('Logout/', views.logout_user , name="logout"),
    path('Accounts/',views.display_account_page, name="accounts"),
    path('SearchResults/',views.display_search_results_page, name="searchresults")
    
]