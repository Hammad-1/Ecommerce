from django import forms

class Detail(forms.Form):

    name = forms.CharField(max_length=64)
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=128)
    email = forms.EmailField()
    postal_code = forms.IntegerField()