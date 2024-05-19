from django.views.generic import TemplateView


# Create your views here.
class BlogListView(TemplateView):
    template_name = 'blogs/blog-list.html'
