from django.contrib import admin
from orders.models import OrdersModel, OrderItemModel

@admin.register(OrdersModel)
class OrdersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'status' , 'created_at']
    list_filter = ['id', 'status' , 'created_at']


@admin.register(OrderItemModel)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'quantity', 'price' , 'size']
    search_fields = ['product_name']

