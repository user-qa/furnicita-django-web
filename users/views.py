import random
import pytz
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from users.forms import RegisterForm, EmailVerificationForm
from users.models import ConfirmationCodesModel

UserModel = get_user_model()

def send_confirmation_email(user):
    random_code = random.randint(100000, 999999)
    active_code = ConfirmationCodesModel.objects.filter(code=random_code).exists()
    if active_code:
        send_confirmation_email(user)
    else:
        ConfirmationCodesModel.objects.create(
            code=random_code,
            user=user
        )
        try:
            send_mail(message=str(random_code), subject='Confirmation Code', recipient_list=[user.email],
                      from_email=settings.EMAIL_HOST_USER)
            return True

        except ConnectionError as e:
            return False


def verify_email(request):
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        return render(request, 'users/verify-email.html')
    else:
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            received_code = form.cleaned_data["code"]
            user_and_code = ConfirmationCodesModel.objects.filter(code=received_code).first()
            if user_and_code:
                time_now = datetime.now(pytz.timezone(settings.TIME_ZONE))
                sent_time = user_and_code.created_at.astimezone(pytz.timezone(settings.TIME_ZONE)) + timedelta(minutes=2)
                if sent_time > time_now:
                    db_user = UserModel.objects.filter(id=user_and_code.user.id).first()
                    db_user.is_active = True
                    user_and_code.delete()
                    return redirect('users:login')

                else:
                    messages.error(request, 'Confirmation Code is expired')
            else:
                messages.error(request, 'The Code Is Invalid')

        else:
            messages.error(request, 'Wrong Password')
        return redirect('users:verify_email')


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:verify_email')

    def form_valid(self, form):
        storage = messages.get_messages(self.request)
        storage.used = True
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        if send_confirmation_email(user):
            return redirect(self.success_url)
        else:
            messages.error(self.request, 'The email could not be sent! Please Try again Later!')
            return redirect(self.success_url)

    def form_invalid(self, form):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.error(request=self.request, message=form.errors)
        return redirect('users:register')



class LoginView(TemplateView):
    template_name = 'users/login.html'


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('pages:home')


class WishlistView(TemplateView):
    template_name = 'users/wishlist.html'


class CartView(TemplateView):
    template_name = 'users/cart.html'


class ChangePasswordView(TemplateView):
    template_name = 'users/reset-password.html'


class AccountView(TemplateView):
    template_name = 'users/account.html'


class CheckoutView(TemplateView):
    template_name = 'products/checkout.html'
