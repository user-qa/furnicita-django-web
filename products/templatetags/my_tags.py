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
    if pk in cart:
        return True
    return False


@register.filter
def total_price(request):
    cart = request.session.get('cart', [])
    products = ProductsModel.objects.filter(id__in=cart)

    total_price_sum = sum([product.real_price for product in products])
    return total_price_sum


@register.filter
def in_wishlist(request, pk):
    wishlist = request.session.get('wishlist', [])
    if pk in wishlist:
        return True
    else:
        return False
