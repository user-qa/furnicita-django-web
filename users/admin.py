from django.contrib import admin
from users.models import ConfirmationCodesModel, AccountModel

@admin.register(ConfirmationCodesModel)
class ConfirmationCodesModelAdmin(admin.ModelAdmin):
    search_fields = ['code', 'created_at']
    list_display = ['code', 'created_at']


@admin.register(AccountModel)
class AccountModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'country', 'city', 'company']
    list_filter = ['full_name', 'phone', 'country', 'city', 'company']
    search_fields = ['full_name', 'phone', 'country', 'city', 'company']
