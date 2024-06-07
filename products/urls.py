from django.urls import path
from products.views import ProductsListView, ProductDetailView, CommentsView
from users.views import add_or_remove, add_or_remove_from_wishlist

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('details/<int:pk>/', ProductDetailView.as_view(), name='details'),
    path('cart/<int:pk>/', add_or_remove, name='add_or_remove'),
    path('wishlist/<int:pk>/', add_or_remove_from_wishlist, name='add_or_remove_from_wishlist'),
    path('comment/<int:pk>/', CommentsView.as_view(), name='comment'),
]