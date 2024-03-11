from django.contrib import admin
from django.urls import path
from products.views import (product_create_view,
                            product_detail_view,
                            render_initial_data,
                            dynamic_lookup_view,
                            product_delete_view,
                            product_list_view
                            )

app_name = 'products'

urlpatterns = [
    path('create', render_initial_data, name='product-create'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete', product_delete_view, name='product-delete'),
    path('', product_list_view, name='products-list')
]
