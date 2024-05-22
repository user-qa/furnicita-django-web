from django.contrib import admin

from pages.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_filter = ['email', 'created_at']
    list_display = ['full_name', 'email', 'created_at']
