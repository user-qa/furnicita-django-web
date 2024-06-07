from django import forms

from blogs.models import BlogCommentsModel


class BlogCommentsModelForm(forms.ModelForm):
    class Meta:
        model = BlogCommentsModel
        fields = ['message']
