from django.db import models

# Create your models


class Category(models.Model):
    
    name = models.CharField(max_length=50)
    
    def __str__(self):
        
        return str(self.name)

def image_upload_book(instance, filename):
    
    """
    Generate the file path for uploaded images.
    """
    try:
        imagename, extension = filename.rsplit('.', 1)
    except ValueError:
        # If the filename has no dots or multiple dots, set default values
        imagename, extension = filename, 'png'  # You can set any default extension

    return f'book/{instance.id}.{extension}'

def image_upload_author(instance, filename):
    
    """
    Generate the file path for uploaded images.
    """
    try:
        imagename, extension = filename.rsplit('.', 1)
    except ValueError:
        # If the filename has no dots or multiple dots, set default values
        imagename, extension = filename, 'png'  # You can set any default extension

    return f'author/{instance.id}.{extension}'

class Book(models.Model):
    

    
    STATUS= [
        ('availbale', 'availbale'),
        ('rented', 'rented'),
        ('sold', 'sold'),
    ]
    
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True)
    photo_author = models.ImageField(upload_to=image_upload_author, null=True, blank=True)
    photo_book = models.ImageField(upload_to=image_upload_book, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=STATUS ,null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self):
        
        return str(self.title)