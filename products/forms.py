from django import forms
from products.models import ProductCommentsModel

class ProductCommentsModelForm(forms.ModelForm):
    class Meta:
        model =ProductCommentsModel
        fields = ['message']