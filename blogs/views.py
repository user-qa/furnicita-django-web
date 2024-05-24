from django.views.generic import TemplateView
from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


# Create your views here.
class BlogListView(TemplateView):
    template_name = 'blogs/blog-list.html'

    def get_context_data(self, **kwargs):
        blogs = BlogModel.objects.all().order_by('-created_at')
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')

        if cat:
            blogs = blogs.filter(categories=cat)
        if tag:
            blogs = blogs.filter(tags=tag)

        categories = BlogCategoryModel.objects.all()
        famous_posts = BlogModel.objects.all().order_by()[:2]
        tags = BlogTagModel.objects.all()
        context = {
            'categories': categories,
            'blogs': blogs,
            'famous_posts': famous_posts,
            'tags': tags,
        }

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

