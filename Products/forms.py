from django import forms 
from Products.models import *


class ProductForm(forms.ModelForm):
    Description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    Manufactured_Date = forms.DateField(
        widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),
),
)
    Expiry_Date = forms.DateField(
        widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),
),
)    
    class Meta:
        model = Product
        fields = "__all__"

        
class ShelfForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))

    class Meta:
        model = Shelf
        fields = '__all__'


class DistributorForm(forms.ModelForm):
    
    class Meta:
        model = Distributor
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
    
    
