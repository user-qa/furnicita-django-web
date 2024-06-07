# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView, CreateView

from .forms import BlogCommentsModelForm
from .models import BlogModel, BlogCategoryModel, BlogTagModel


class BlogListView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'
    paginate_by = 2


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

    def get_queryset(self):
        blogs = BlogModel.objects.all().order_by('-created_at')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')
        if tag:
            blogs = blogs.filter(tags__in=tag)

        if cat:
            blogs = blogs.filter(categories__id=cat)  # Assuming categories and tags are foreign keys
        if tag:
            blogs = blogs.filter(tags__id=tag)

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
        context['related_posts'] = BlogModel.objects.filter(categories__in=context['blog'].categories.all()).exclude(id=context['blog'].id).distinct()[:3]

        return context


class BlogCommentsView(LoginRequiredMixin, CreateView):
    template_name = 'blogs/detail.html'
    form_class = BlogCommentsModelForm
    login_url = 'users:login'

    def get_success_url(self):
        next = self.request.POST.get('next')
        return next

    def form_valid(self, form):
        blog_id = self.request.POST.get('blog_id')
        blog = BlogModel.objects.get(id=blog_id)
        current_user = self.request.user

        comment = form.save(commit=False)
        comment.user = current_user
        comment.blog = blog
        comment.save()

        return redirect(self.get_success_url())


    def form_invalid(self, form):
        print(form.errors)
        return redirect(self.get_success_url())



