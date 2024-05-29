from django.views.generic import TemplateView, ListView
from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


# Create your views here.
from django.views.generic import ListView
from .models import BlogModel, BlogCategoryModel, BlogTagModel


class BlogListView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'
    paginate_by = 2

    def get_queryset(self):
        blogs = BlogModel.objects.all().order_by('-created_at')
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')

        if cat:
            blogs = blogs.filter(categories__id=cat)  # Assuming categories and tags are foreign keys
        if tag:
            blogs = blogs.filter(tags__id=tag)

        return blogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = BlogCategoryModel.objects.all()
        famous_posts = BlogModel.objects.all().order_by('-created_at')[:2]
        tags = BlogTagModel.objects.all()

        context['categories'] = categories
        context['famous_posts'] = famous_posts
        context['tags'] = tags
        return context


class BlogDetailView(TemplateView):
    template_name = 'blogs/detail.html'

    def get_context_data(self, **kwargs):
        categories = BlogCategoryModel.objects.all()
        blog = BlogModel.objects.get(pk=self.kwargs["pk"])
        famous_posts = BlogModel.objects.all().order_by()[:2]
        tags = BlogTagModel.objects.all()
        context = {
            'categories': categories,
            'blog': blog,
            'famous_posts': famous_posts,
            'tags': tags,
            'related_blogs': BlogModel.objects.filter(categories__in=blog.categories.all())[:3]

        }

        return context

