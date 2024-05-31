from django.contrib import admin
from users.models import ConfirmationCodesModel

@admin.register(ConfirmationCodesModel)
class ConfirmationCodesModelAdmin(admin.ModelAdmin):
    search_fields = ['code', 'created_at']
    list_display = ['code', 'created_at']