from django import forms
from .models import *

class BookForm(forms.ModelForm):
    
    class Meta:
        
        model = Book
        
        fields = "__all__"
        exclude = ('active',)
        
class CatForm(forms.ModelForm):
    
    class Meta:
        
        model = Category
        
        fields = ['name']
