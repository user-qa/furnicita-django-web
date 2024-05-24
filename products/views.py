from django.views.generic import TemplateView

from products.models import ManufacturerModel, CatalogModel, ColorModel, TagModel, ProductsModel


class ProductsListView(TemplateView):
    template_name = 'products/product-list.html'

    def get_context_data(self, **kwargs):
        products = ProductsModel.objects.all()
        tags = TagModel.objects.all()
        catalogs = CatalogModel.objects.all()
        catalogs_with_counts = [{'name': catalog, 'count': products.filter(catalogs__name=catalog.name).count()} for
                                catalog in catalogs]
        manufacturers = ManufacturerModel.objects.all()
        manufacturers_with_counts = [
            {'name': manufacture, 'count': products.filter(manufacturer__name=manufacture.name).count()} for manufacture
            in manufacturers]
        colors = ColorModel.objects.all()
        color_with_counts = [{'name': color, 'count': products.filter(color__name=color.name).count()} for color in
                             colors]

        col = self.request.GET.get('col')
        if col:
            products = products.filter(color__id=col)

        tag = self.request.GET.get('tag')
        if tag:
            products = products.filter(tags__id=tag)

        context = {
            'products': products,
            'tags': tags,
            'catalogs_with_counts': catalogs_with_counts,
            'manufacturers_with_counts': manufacturers_with_counts,
            'color_with_counts': color_with_counts
        }

        return context


class ProductDetailView(TemplateView):
    template_name = 'products/product-detail.html'

    def get_context_data(self, **kwargs):
        product = ProductsModel.objects.get(id=self.kwargs["pk"])
        context = {
            'product': product,
            'sizes': product.size.all(),
            'colors':product.color.all(),
            'tags': product.tags.all(),
            'categories': product.catalogs.all(),

            'all_tags':TagModel.objects.all()
        }

        return context


