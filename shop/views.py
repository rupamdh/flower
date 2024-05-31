from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def category_details(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    cat_ids = [1, 9, 22]
    categories = Category.objects.filter(id__in=cat_ids)
    subcategories = Category.objects.filter(parent=cat)


    context = {
        'cat' : cat,
        'categories' : categories,
        'subcategories' : subcategories
    }
    return render(request, 'shop/category-details.html', context)