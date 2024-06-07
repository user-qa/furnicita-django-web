from django.contrib import admin

from blogs.models import AuthorModel, BlogCategoryModel, BlogModel, BlogTagModel, BlogCommentsModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_filter = ['name', 'position', 'profession', 'created_at']
    list_display = ['name', 'position', 'profession', 'created_at']
    search_fields = ['name', 'position', 'profession', 'created_at']


@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_filter = ['name', 'created_at']
    list_display = ['name', 'created_at']
    search_fields = ['name', 'created_at']


@admin.register(BlogTagModel)
class BlogTagModelAdmin(admin.ModelAdmin):
    list_filter = ['name', 'created_at']
    list_display = ['name', 'created_at']
    search_fields = ['name', 'created_at']


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_filter = ['title', 'created_at']
    list_display = ['title', 'created_at']
    search_fields = ['title', 'created_at']

@admin.register(BlogCommentsModel)
class BlogCommentsModelAdmin(admin.ModelAdmin):
    list_filter = ['message', 'created_at']
    list_display = ['message', 'created_at']
    search_fields = ['message', 'created_at']