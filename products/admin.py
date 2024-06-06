from django.contrib import admin

from products.models import ManufacturerModel, CatalogModel, SizeModel, ColorModel, TagModel, ProductsModel, \
    ProductImagesModel, ProductCommentsModel


@admin.register(ManufacturerModel)
class ManufacturerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'created_at']


@admin.register(CatalogModel)
class CatalogModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'created_at']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'created_at']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'created_at']


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'created_at']


class ProductImagesModelAdmin(admin.StackedInline):
    model = ProductImagesModel


@admin.register(ProductsModel)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'price', 'sku', 'created_at']
    list_filter = ['name', 'count', 'sku', 'created_at']
    search_fields = ['name', 'count', 'sku', 'created_at']
    inlines = [ProductImagesModelAdmin]
    readonly_fields = ['real_price']

@admin.register(ProductCommentsModel)
class ProductCommentsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']

