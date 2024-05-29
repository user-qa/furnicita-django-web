from django.views.generic import TemplateView, ListView

from products.models import ManufacturerModel, CatalogModel, ColorModel, TagModel, ProductsModel


class ProductsListView(ListView):
    template_name = 'products/product-list.html'
    context_object_name = 'products'
    model = ProductsModel
    paginate_by = 2

    def get_queryset(self):
        products = ProductsModel.objects.all()
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')

        if tag:
            products = products.filter(tags__in=tag)
        if cat:
            products = products.filter(categories__in=cat)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogs'] = CatalogModel.objects.all()
        context['colors'] = ColorModel.objects.all()

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


