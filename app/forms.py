from django import forms
from .models import *

class BookForm(forms.ModelForm):
    
    class Meta:
        
        model = Book
        
        fields = "__all__"
        exclude = ('active',)
        widgets = {
            "retal_price_day": forms.NumberInput(attrs={'class':'form-control','id':'retalprice'}),
            "retal_period": forms.NumberInput(attrs={'class':'form-control','id':'retaldays'}),
            "total_rental": forms.NumberInput(attrs={'class':'form-control','id':'totalrental'}),
        }
        
class CatForm(forms.ModelForm):
    
    class Meta:
        
        model = Category
        
        fields = ['name']
