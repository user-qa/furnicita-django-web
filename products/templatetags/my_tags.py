from django import template

from products.models import ProductsModel

register = template.Library()


@register.filter
def get_user_cart(request):
    cart = request.session.get('cart', [])
    products = ProductsModel.objects.filter(pk__in=cart)
    return products


@register.filter
def in_cart(request, pk):
    cart = request.session.get('cart', [])
    print(pk)
    print(cart)
    if pk in cart:
        return True
    return False
