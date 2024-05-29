from django.views.generic import TemplateView, ListView
from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


# Create your views here.
class BlogListView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'
    model = BlogModel
    paginate_by = 2

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
        context['categories'] = BlogCategoryModel.objects.all()
        context['recent_posts'] = BlogModel.objects.all()[:2]
        context['tags'] = BlogTagModel.objects.all()

        return context


class BlogDetailView(ListView):
    template_name = 'blogs/detail.html'
    context_object_name = 'blog'

    def get_queryset(self):
        blog = BlogModel.objects.get(id=self.kwargs["pk"])
        return blog

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategoryModel.objects.all()
        context['recent_posts'] = BlogModel.objects.exclude(id=self.kwargs["pk"])[:2]
        context['tags'] = BlogTagModel.objects.all()

        return context

