from django.contrib import admin
from .models import Language, Category, Product, ProductImage
# Register your models here.



class ProductAdmin (admin.ModelAdmin):
    list_display = (
    'name',
    'publisher', 
    'author', 
    'year_of_publication',
    'isbn',
    'price',
    )

    ording = ('name',) 

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Language)
admin.site.register(Category)
