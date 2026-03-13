from django.contrib import admin
from django.urls import path
from products.views import product_list, product_detail
from categories.views import category_list

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Mahsulotlar uchun manzillar
    path('products/', product_list),
    path('products/detail/', product_detail),
    
    # Kategoriyalar uchun manzil
    path('categories/', category_list),
]