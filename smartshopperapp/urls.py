from django.urls import path
from . import views

urlpatterns = [
    path('' , views.display_home_page ),
    path('CreateList/' , views.display_create_list_page),
    path('SelectCategory/', views.display_category_page),
    path('Catalogue/<category>/' , views.display_catalogue_page)
    
]