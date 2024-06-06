from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView

from orders.forms import OrderModelForm
from orders.models import OrderItemModel
from orders.models import OrdersModel
from products.models import ProductsModel

UserModel = get_user_model()


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'products/checkout.html'
    login_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', None)
        if cart is None:
            return redirect('products:list')
        products = ProductsModel.objects.filter(id__in=cart)
        total_price = sum([product.real_price for product in products])
        context.update({
            'number_of_products': len(cart),
            'total_price': total_price,
        })

        return context


@login_required
def order_create_view(request):
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            new_order = OrdersModel.objects.create(
                user=request.user,
                status=False
            )
            cart = request.session.get('cart', None)
            products = ProductsModel.objects.filter(pk__in=cart)
            for product in products:
                OrderItemModel.objects.create(
                    product=product,
                    product_name=product.name,
                    quantity=1,
                    size='test',
                    price=product.real_price,
                    order=new_order,
                    image1=product.image1,
                    image2=product.image2,
                )
            request.session['cart'] = []
            return redirect('products:list')
        else:
            return redirect('orders:checkout')


class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'users/order-history.html'
    context_object_name = 'my_orders'
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        my_orders = OrdersModel.objects.filter(user=self.request.user)
        return my_orders
