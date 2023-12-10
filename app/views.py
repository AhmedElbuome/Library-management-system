from django.shortcuts import render
from .models import *
# Create your views here.

#? index function
def index(request):
    
    forms = Book.objects.all()
    
    context= {
        'forms':forms
    }
    
    return render(request, 'app/index.html', context)

#? books function
def books(request):
    
    return render(request, 'app/books.html', {})
