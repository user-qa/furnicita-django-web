from django import forms


class OrderModelForm(forms.Form):
    address = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=128)
