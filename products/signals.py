from django.db.models.signals import pre_save
from django.dispatch import receiver

from products.models import ProductsModel

@receiver(signal=pre_save,sender=ProductsModel)
def calculate_real_price(sender, instance, **kwargs):
    instance.real_price = instance.price - instance.discount * instance.price / 100