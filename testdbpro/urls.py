"""testdbpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dbapp import views
from django.urls import path

urlpatterns = [
  path('',views.addProduct,name='addProduct'),
  path('add_product_details',views.add_product_details,name='add_product_details'),
  path('show_products',views.show_products,name='show_products'),
  path('editpage/<int:pk>',views.editpage,name='editpage'),
  path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
  path('edit_product_details/<int:pk>',views.edit_product_details,name='edit_product_details'),
  path('delete_product/<int:pk>',views.delete_product,name='delete_product')
]
