from django.forms import ModelForm
from .models import Courses, Product
from django import forms

class CoursesForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'price', 'description', 'image']


class AddressForm(forms.Form):
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image']