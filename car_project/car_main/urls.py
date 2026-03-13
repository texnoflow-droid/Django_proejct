# """
# URL configuration for car_main project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/6.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path
from cars.views import car_list, car_info
from spore_parts.views import spare_parts_info, spare_parts_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', car_list, name='car_list'),
    path('cars/car_info/', car_info, name='car_info'),
    path("spore_parts/", spare_parts_list, name="spare_parts_list"),
    path("spore_parts_info/<int:spare_part_id>/", spare_parts_info, name="spare_parts_info")
]