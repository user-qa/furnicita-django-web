from django.contrib.auth import get_user_model
from django.db import models

from products.models import ProductsModel

UserModel = get_user_model()


class OrdersModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, related_name='orders')
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrdersModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductsModel, on_delete=models.SET_NULL, null=True, related_name='orders')

    product_name = models.CharField(max_length=255)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=128)
    image1 = models.ImageField(upload_to='orders')
    image2 = models.ImageField(upload_to='orders')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
