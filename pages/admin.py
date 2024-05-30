from django.contrib import admin

from pages.models import ContactModel, MainPageCommentsModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_filter = ['email', 'created_at']
    list_display = ['full_name', 'email', 'created_at']


@admin.register(MainPageCommentsModel)
class MainPageCommentsModelAdmin(admin.ModelAdmin):
    list_filter = ['person_name', 'created_at']
    list_display = ['person_name', 'created_at']
