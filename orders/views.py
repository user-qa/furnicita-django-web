from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from orders.forms import OrderModelForm
from orders.models import OrdersModel
from products.models import ProductsModel
from users.models import AccountModel
from orders.models import OrderItemModel

UserModel = get_user_model()


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'products/checkout.html'
    login_url = reverse_lazy('users:login')


@login_required
def order_create_view(request):
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            new_order = OrdersModel.objects.create(
                user = request.user,
                status = False
            )

            cart = request.session.get('cart', None)
            if cart is None:
                return redirect('products:list')
            products = ProductsModel.objects.filter(pk__in=cart)
            for product in products:
                OrderItemModel.objects.create(
                    product = product,
                    product_name= product.name,
                    quantity = 1,
                    size = 'test',
                    price = product.real_price,
                    order = new_order,
                    image1 = product.image1,
                    image2 = product.image2,
                )
            request.session['cart'] = []
            return redirect('products:list')
        else:
            return redirect('products:checkout')




