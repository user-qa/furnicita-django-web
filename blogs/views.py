from django.views.generic import TemplateView, ListView
from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


# Create your views here.
class BlogListView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'
    model = BlogModel

    def get_queryset(self):
        blogs = BlogModel.objects.all().order_by('-created_at')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')
        if tag:
            blogs = blogs.filter(tags__in=tag)

        if cat:
            blogs = blogs.filter(categories__in=cat)

        return blogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class BlogDetailView(TemplateView):
    template_name = 'blogs/detail.html'

