from django.views.generic import TemplateView

from products.models import ManufacturerModel, CatalogModel, ColorModel, TagModel, ProductsModel


class ProductsListView(TemplateView):
    template_name = 'products/product-list.html'


class ProductDetailView(TemplateView):
    template_name = 'products/product-detail.html'



