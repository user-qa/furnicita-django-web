from django.urls import path
from products.views import ProductsListView, ProductDetailView
from users.views import add_or_remove

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('details/<int:pk>/', ProductDetailView.as_view(), name='details'),
    path('cart/<int:pk>/', add_or_remove, name='add_or_remove'),
]