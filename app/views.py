from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

#? index function
def index(request):
    if request.method == "POST":
        
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
        form2 = CatForm(request.POST)
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
        'form2':CatForm(),
        'book_count': Book.objects.filter(active=True).count(),
        'book_sold': Book.objects.filter(status='sold').count(),
        'book_rented': Book.objects.filter(status='rented').count(),
        'book_availbale': Book.objects.filter(status='availbale').count(),
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

def update(request, id):
    
    book_id = Book.objects.get(id = id)
    
    if request.method == "POST":
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')

    else:
        book_save = BookForm(instance=book_id)
        
    context= {
        'book_save':book_save ,
        'form2':CatForm(),
    }
    
    return render(request, 'app/update.html', context)

def delete(request, id ):
    
    book_delete = get_object_or_404(Book, id = id)
    if request.method == 'POST':
        
        book_delete.delete()
        return redirect('/')
    
    context= {
        'form2':CatForm(),
    }
    
    return render(request, 'app/delete.html', context)