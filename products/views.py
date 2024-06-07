from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from products.forms import ProductCommentsModelForm
from products.models import ManufacturerModel, CatalogModel, ColorModel, TagModel, ProductsModel, ProductCommentsModel


class ProductsListView(ListView):
    template_name = 'products/product-list.html'
    context_object_name = 'products'
    model = ProductsModel
    paginate_by = 10

    def get_queryset(self):
        products = ProductsModel.objects.all().order_by('-created_at')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')
        col = self.request.GET.get('col')
        man = self.request.GET.get('man')
        sort = self.request.GET.get('sort')
        q = self.request.GET.get('q')

        if tag:
            products = products.filter(tags__in=tag)
        if cat:
            products = products.filter(catalogs__in=cat)
        if col:
            products = products.filter(color__in=col)
        if man:
            products = products.filter(manufacturer=man)
        if sort:
            if sort == 'a2z':
                products = products.order_by('name')
            if sort == 'z2a':
                products = products.order_by('-name')
            if sort == 'l2h':
                products = products.order_by('real_price')
            if sort == 'h2l':
                products = products.order_by('-real_price')
        if q:
            products = products.filter(name__icontains=q)

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
        product = ProductsModel.objects.get(pk=self.kwargs['pk'])
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


class CommentsView(LoginRequiredMixin, CreateView):
    template_name = 'products/product-detail.html'
    form_class = ProductCommentsModelForm
    login_url = 'users:login'

    def get_success_url(self):
        next = self.request.POST.get('next')
        return next

    def form_valid(self, form):
        product_id = self.kwargs["pk"]
        product = ProductsModel.objects.get(id=product_id)
        current_user = self.request.user

        comment = form.save(commit=False)
        comment.user = current_user
        comment.product = product
        comment.save()

        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return redirect(self.get_success_url())

