from django import forms

class PostCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=32, min_length=3)
    rate = forms.FloatField(max_value=5)
    description = forms.CharField(widget=forms.Textarea())

class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=40, min_length=5)
    price = forms.FloatField(max_value=1000)
    compound = forms.CharField(widget=forms.Textarea())

class ReviewCreateForm(forms.Form):
    nickname = forms.CharField(max_length=40, min_length=10)
    country = forms.CharField(max_length=60, min_length=10)
    comment = forms.CharField(max_length=350, min_length=1)
    grade = forms.FloatField( max_value=5)
    created_data = forms.DateTimeField(input_formats=None)
#
class CategoryCreateForm(forms.Form):
    kind_food = forms.CharField(max_length=50, min_length=10)
    count = forms.IntegerField(max_value=1000, min_value=10)