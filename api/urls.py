from django.urls import path
from .views import get_product_category, get_user_details, get_product_lone, get_products, create_user
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views

urlpatterns=[
    path('', get_products), 
    path('obtain_auth_token', views.obtain_auth_token), 
    path('get_user_details', get_user_details),
    path('register', create_user),
    path('get_product_lone', get_product_lone), 
    path('get_product_category', get_product_category)
]