from django.db.models import Q
from django.views.generic import ListView

from products.models import ManufacturerModel, CatalogModel, ColorModel, TagModel, ProductsModel


class ProductsListView(ListView):
    template_name = 'products/product-list.html'
    context_object_name = 'products'
    model = ProductsModel
    paginate_by = 2

    def get_queryset(self):
        products = ProductsModel.objects.all().order_by('-created_at')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')
        col = self.request.GET.get('col')
        man = self.request.GET.get('man')
        sort = self.request.GET.get('sort')


        if tag:
            products = products.filter(tags__in=tag)
        if cat:
            products = products.filter(catalogs__in=cat)
        if col:
            products = products.filter(color__in=col)
        if man:
            products = products.filter(manufacturer=man)
        if sort:
            products = products.order_by(sort)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CatalogModel.objects.all()
        context['manufacturers'] = ManufacturerModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        context['tags'] = TagModel.objects.all()

        return context


class ProductDetailView(ListView):
    template_name = 'products/product-detail.html'
    context_object_name = 'product'
    model = ProductsModel

    def get_queryset(self):
        product = ProductsModel.objects.get(id=self.kwargs["pk"])
        return product

    def get_related_products(self):
        product = ProductsModel.objects.get(id=self.kwargs["pk"])
        product_tags = product.tags.all()
        product_categories = product.catalogs.all()

        tag_condition = Q(tags__in=product_tags)
        category_condition = Q(catalogs__in=product_categories)

        related_products = ProductsModel.objects.filter(tag_condition | category_condition).exclude(
            id=product.id).distinct()[:3]
        return related_products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CatalogModel.objects.all()
        context['tags'] = TagModel.objects.all()
        context['related_products'] = self.get_related_products()

        return context
