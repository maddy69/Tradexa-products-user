from django.urls import path
from products import views

urlpatterns = [
    path('product_list/', views.list, name = 'products_page'),
]