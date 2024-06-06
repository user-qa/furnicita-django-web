from django.urls import path
from orders.views import CheckoutView, order_create_view, OrderHistoryView

app_name = 'orders'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order/', order_create_view, name='order'),
    path('history/', OrderHistoryView.as_view(), name='history'),
]