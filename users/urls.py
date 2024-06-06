from django.urls import path

from users.views import RegisterView, LoginView, AccountView, WishlistView, CartView, ChangePasswordView, logout_view, verify_email

app_name = 'users'

urlpatterns = [
    path('account/', AccountView.as_view(), name='account'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change/password/', ChangePasswordView.as_view(), name='change-password'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('cart/', CartView.as_view(), name='cart'),
    path('verify-email/', verify_email, name='verify_email')
]
