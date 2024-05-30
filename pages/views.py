from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from pages.models import MainPageCommentsModel

from pages.forms import ContactModelForm


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {
            'pro_comments': MainPageCommentsModel.objects.all()
        }

        return context



class ContactTemplateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def form_invalid(self, form):
        errors = form.errors
        for error in errors:
            messages.error(self.request, f"{error.title()} field must be filled")
        return redirect('pages:contact')

    def form_valid(self, form):
        form = ContactModelForm(self.request.POST)
        form.save()

        messages.success(self.request, 'Your message is successfully sent!')
        return redirect('pages:contact')




