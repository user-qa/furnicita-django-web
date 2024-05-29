from django.views.generic import TemplateView, ListView

from products.models import ManufacturerModel, CatalogModel, ColorModel, TagModel, ProductsModel


class ProductsListView(ListView):
    template_name = 'products/product-list.html'
    context_object_name = 'products'
    model = ProductsModel

    def get_queryset(self):
        products = ProductsModel.objects.all().order_by('-created_at')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')

        if tag:
            products = products.filter(tags__in=tag)
        if cat:
            products = products.filter(catalogs__in=cat)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CatalogModel.objects.all()
        context['manufacturers'] = ManufacturerModel.objects.all()
        context['colors'] = ColorModel.objects.all()






        return context










class ProductDetailView(TemplateView):
    template_name = 'products/product-detail.html'
