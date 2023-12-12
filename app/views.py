from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

#? index function
def index(request):
    
    if request.method == "POST":
        
        form = BookForm(request.POST, request.FILES)
        form2 = CatForm(request.POST)
        if form.is_valid():
            form.save()
            
        if form2.is_valid():
            form2.save()
    else:
        form = BookForm()
        form2 = CatForm()
    
    books = Book.objects.all()
    category = Category.objects.all()
    
    context= {
        'books':books,
        'category':category,
        'form':form,
        'form2':form2,
    }
    
    return render(request, 'app/index.html', context)

#? books function
def books(request):
    
    category = Category.objects.all()
    books = Book.objects.all()
    
    context= {
        'category':category,
        'books':books ,
    }
        
    return render(request, 'app/books.html', context)
